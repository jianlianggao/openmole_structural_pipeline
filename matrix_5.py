import sys, os.path
import numpy
from numpy import *
from array import *
import csv

input = open(sys.argv[1],'r')
#n = float(sys.argv[2])

#print("reading the matrix")
data = csv.reader(input, delimiter="\t")
headers = next(data, None)

array = numpy.array(list(data)).astype(str)

array = array[:,[0,2]]

array1 = numpy.array([[sys.argv[2]]]) #add subject ID

for ii in range(array1.shape[0], array.shape[0]):
  array1 = numpy.append(array1, array1, axis = 0)
  
array = numpy.append(array1, array, axis = 1)

print(array)
#print(n)
#mult = array * n

#define a new array with dtype object to store T1 and T2 parameters
arrayTemp = numpy.empty((array.shape[0],array.shape[1]+2), dtype='object')
arrayTemp[:, 0:array.shape[1]] = array

# check if T1 or T2 nifti files exist or not
for ii in range(0, array.shape[0]):
  T1path = '/data/'+array[ii,0]+'/ses-'+array[ii,1]+'/anat/'+array[ii,0]+'_ses-'+array[ii,1]+'_T1w.nii.gz'
  if os.path.exists(T1path):
    arrayTemp[ii, array.shape[1]] = '-T1 '+T1path
  else:
    arrayTemp[ii, array.shape[1]] = ' '
  T2path = '/data/'+array[ii,0]+'/ses-'+array[ii,1]+'/anat/'+array[ii,0]+'_ses-'+array[ii,1]+'_T2w.nii.gz'
  if os.path.exists(T2path):
    arrayTemp[ii, array.shape[1]+1] = '-T2 '+T2path
  else:
    arrayTemp[ii, array.shape[1]+1] = ' '

#print("saving the matrix")
#numpy.savetxt(sys.argv[3], mult, fmt='%g')
# save to  file
title_str =  numpy.array([["subject_ID", "session_ID", "scan_age", "T1_para", "T2_para"]])

if (not os.path.exists(sys.argv[3])):
  arrayTemp= numpy.append(title_str, arrayTemp, axis=0)

file_handle = open(sys.argv[3], 'a')
numpy.savetxt(file_handle,arrayTemp, delimiter=',', fmt='%s')
file_handle.close()