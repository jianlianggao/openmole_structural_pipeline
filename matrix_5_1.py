## This Python code works only with data path in 
## /vol/dhcp-reconstructed-images/UpdatedReconstructions/ReconstructionsRelease03/
## to find T1MS_Co3DOutSVRMot.nii and T2MS_Co3DOutSVRMot.nii files.

import sys, os.path
import numpy
from numpy import *
from array import *
import csv

input = open(sys.argv[1],'r')
#n = float(sys.argv[2])
#debug
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

#print("reading the matrix")
data = csv.reader(input, delimiter="\t")
headers = next(data, None)

array = numpy.array(list(data)).astype(str)
array1 = numpy.array([[sys.argv[2]]]) #add subject ID
#debug
print("======")
print(array)
print(array1)
print(array[:,[0,2]])
print("======")

try:

  array = array[:,[0,2]]

  array1tmp = array1

  for ii in range(array1.shape[0], array.shape[0]):
    array1 = numpy.append(array1, array1tmp, axis = 0)

  print("====")
  print(array)
  print(array.shape)
  print("subject ID matrix expanded:")  
  print(array1)
  print(array1.shape)

  array = numpy.append(array1, array, axis = 1)

  #print(array)
  #print(array.shape)
  #print(array1)
  #print(array1.shape)
  #print(n)
  #mult = array * n

  #define a new array with dtype object to store T1 and T2 parameters
  arrayTemp = numpy.empty((array.shape[0],array.shape[1]+2), dtype='object')
  arrayTemp[:, 0:array.shape[1]] = array
  
  title_str =  numpy.array([["subject_ID", "session_ID", "scan_age", "T1_para", "T2_para"]])

  # check if T1 or T2 nifti files exist or not
  for ii in range(0, array.shape[0]):
    T1path = '/data/'+array[ii,0]+'/ses-'+array[ii,1]+'/T1MS/'+array[ii,0]+'_ses-'+array[ii,1]+'_T1MS_T1MS_Co3DOutSVRMot.nii'
    if os.path.exists(T1path):
      arrayTemp[ii, array.shape[1]] = '-T1 '+T1path
    else:
      arrayTemp[ii, array.shape[1]] = ' '
    T2path = '/data/'+array[ii,0]+'/ses-'+array[ii,1]+'/T2MS/'+array[ii,0]+'_ses-'+array[ii,1]+'_T2MS_T2MS_Co3DOutSVRMot.nii'
    if os.path.exists(T2path):
      arrayTemp[ii, array.shape[1]+1] = '-T2 '+T2path
      if (not os.path.exists(sys.argv[3])):
        arrayTemp1= numpy.append(title_str, arrayTemp[[ii],:], axis=0)
      else:
        arrayTemp1= arrayTemp[[ii],:]

      file_handle = open(sys.argv[3], 'a')
      numpy.savetxt(file_handle,arrayTemp1, delimiter=',', fmt='%s')
      file_handle.close()
    else:
      arrayTemp[[ii], array.shape[1]+1] = 'T2 imaging file not found'
      file_handle = open("/data/error_log.csv", 'a')
      numpy.savetxt(file_handle, arrayTemp[[ii],:], delimiter=',', fmt='%s')
      file_handle.close()
      #arrayTemp[ii, array.shape[1]+1] = ' '

  #print("saving the matrix")
  #numpy.savetxt(sys.argv[3], mult, fmt='%g')
  # save to  file

  

  
  
except IndexError:
  file_handle = open("/data/error_log.csv", 'a')
  numpy.savetxt(file_handle, array1, delimiter=',', fmt='%s')
  file_handle.close()