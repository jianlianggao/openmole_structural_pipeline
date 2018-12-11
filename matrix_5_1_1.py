## This Python code works only with data path in 
## /vol/dhcp-reconstructed-images/UpdatedReconstructions/ReconstructionsRelease03/
## to find T1MS_Co3DOutSVRMot.nii and T2MS_Co3DOutSVRMot.nii files.

import sys, os.path
import numpy
from numpy import *
from array import *
## import csv
##import pip
## error, wont be able to install packages in the Python container used.
##def install(package):
##    if hasattr(pip, 'main'):
##        pip.main(['install', package])
##    else:
##        pip._internal.main(['install', package])
        
##def install_and_import(package):
##    import importlib
##    try:
##        importlib.import_module(package)
##    except ImportError:
##        import pip
##        pip.main(['install', package])
##    finally:
##        globals()[package] = importlib.import_module(package)

##install_and_import('pandas')

#import pandas as pd

input = open(sys.argv[1],'r')
#n = float(sys.argv[2])
#debug
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

#print("reading the matrix")

data=numpy.genfromtxt(input, dtype=None, delimiter='\t', names=True)
array=numpy.array([data['session_id']]).transpose()
array=numpy.reshape(array, (array.shape[0],1))

array11=numpy.array([data['age_at_scan']]).transpose()
array11=numpy.reshape(array11, (array11.shape[0],1))

array=numpy.append(array,  array11, axis=1)


##df=pd.read_csv(input, sep='\t')
##array=df.values



array1 = numpy.array([[sys.argv[2]]]) #add subject ID
#debug
print("======")
print(array)
print(array1)
print(array[:,[0,1]])
print("======")


if array.shape[0]!=0:
  try:

    array = array[:,[0,1]]

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
      T1path = '/data/'+array[ii,0]+'/ses-'+str.split(array[ii,1],sep='.')[0]+'/T1MS/'+array[ii,0]+'_ses-'+str.split(array[ii,1],sep='.')[0]+'_T1MS_T1MS_Co3DOutSVRMot.nii'
      if os.path.exists(T1path):
        arrayTemp[ii, array.shape[1]] = '-T1 '+T1path
      else:
        arrayTemp[ii, array.shape[1]] = ' '
      T2path = '/data/'+array[ii,0]+'/ses-'+str.split(array[ii,1],sep='.')[0]+'/T2MS/'+array[ii,0]+'_ses-'+str.split(array[ii,1],sep='.')[0]+'_T2MS_T2MS_Co3DOutSVRMot.nii'
      #debug
      print(T2path)
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
        #debug
        print('T2 imaging file not found')
        arrayTemp[[ii], array.shape[1]+1] = 'T2 imaging file not found'
        file_handle = open("/data/error_log.csv", 'a')
        numpy.savetxt(file_handle, arrayTemp[[ii],:], delimiter=',', fmt='%s')
        file_handle.close()
        #arrayTemp[ii, array.shape[1]+1] = ' '

  
  except IndexError:
    file_handle = open("/data/error_log.csv", 'a')
    numpy.savetxt(file_handle, array1, delimiter=',', fmt='%s')
    file_handle.close()

else:
  file_handle = open("/data/error_log.csv", 'a')
  numpy.savetxt(file_handle, array1, delimiter=',', fmt='%s')
  file_handle.close()