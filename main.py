#
#    #  #                       #         In the name of God   #    #
#
#
#github.com/cloner174
#cloner174.org@gmail.com
#
#
from flowio import read_multiple_data_sets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
from os.path import exists
from numpy.random import randint
import re

#input_folder = 'data/input'
#output_folder = 'data/output'

#IN_ = 'data/input/data-normal-hum/data-hum/8527 ZOBEYR MOHAMMADI/'
#OUT_ = 'data/output'

#self.output.append(  os.path.join(self.OUTfcs, anyFile[:-4] + '.fcs') )
path = os.path.join(base_path, sub_path)
class nr:
    
    def __init__(self, input_folder, output_folder) :
        
        self.input = []
        self.output = []
        self.store = None
        self.listArrBoth = []
        self.listArr1 = []
        self.listArr2 = []
        self.listFlowData1 = []
        self.listFlowData2 = []
        
        self.inputFolder = input_folder
        self.folderFiles = os.listdir(input_folder)
        csv_ = os.path.join(output_folder,'CSVs')

        print("\n Detecting the folders and subfolders... \n ")
        time.sleep(5)
        if exists( csv_):
            print("\n CSVs folder already exists in output folder. cheking next require folder.. \n ")
            time.sleep(1)
            if exists(os.path.join(csv_, 'additionals')) :
                pass
            else:
                os.mkdir(os.path.join(csv_, 'additionals'))
        else:
            os.mkdir(csv_)
            if exists(os.path.join(csv_, 'additionals')) :
                pass
            else:
                os.mkdir(os.path.join(csv_, 'additionals'))
        if exists( f"{output_folder}/FCSs/" ) :
            print("\n FCSs folder already exists in output folder. cheking next require folder.. \n ")
            time.sleep(1)
        else:
            os.mkdir(f"{output_folder}/FCSs/")
        if exists( f"{output_folder}/FIGs/" ) :
            print("\n FIGs folder already exists in output folder. cheking next require folder.. \n ")
            time.sleep(1)
        else:
            os.mkdir(f"{output_folder}/FIGs/")
        if exists( f"{output_folder}/singleFiles/" ) :
            print("\n etc folder already exists in output folder. cheking next require folder.. \n ")
            time.sleep(1)
        else:
            os.mkdir(f"{output_folder}/singleFiles/")
        
        print( "\n All Done ! \n ")
        time.sleep(2)
        print("\n Finishing up .... \n ")
        time.sleep(3)
        self.OUTcsv = f"{output_folder}/CSVs/"
        self.OtherCSV = f"{output_folder}/CSVs/additionals/"
        self.OUTfcs = f"{output_folder}/FCSs/"
        self.OUTfig = f"{output_folder}/FIGs/"
        self.OUTsingle = f"{output_folder}/singleFiles/"
        
        print( "\n Secssusfully Create The Object. \n ") 
        time.sleep(2)
        print("\n Now you may use any of Functions from this class! \n ")
        time.sleep(2)
    
    
    def get_data(self):
        
        for anyFile in self.folderFiles:
            
            if anyFile.lower().endswith('.lmd'):
                
                self.input.append( os.path.join(self.inputFolder, anyFile) )
    
    
    def read_single_file(self, path) :
        
        try:
            temp = read_multiple_data_sets(path)
        except:
            try:
                temp = read_multiple_data_sets(path, ignore_offset_error = True)
            except:
                raise ValueError("\n Your Provided path is not currect or may be the file is damaged \n Make sure your path is fully represent the path to your data and its format like lmd or fcs \n ")
        
        data1 = temp[0]
        data2 = temp[1]
        
        data1evs = data1.events
        data2evs = data2.events
        
        data1Arr = np.asarray(data1evs)
        data1Arr = data1Arr.reshape( data1.event_count, -1 )
        data2Arr = np.asarray(data2evs)
        data2Arr = data2Arr.reshape( data2.event_count, -1 )
        
        Data = np.concatenate([ data1Arr, data2Arr ], axis = 1)        
        
        self.store = ( Data,data1Arr,data2Arr, data1,data2, str(data1.name))
    
    
    def read_data(self) :
        
        temp = []
        
        for file in self.input :
            
            temp.append( read_multiple_data_sets(file, ignore_offset_error=True) )
            
        for i in range( len( temp )) :
            
            data1 =  temp[i][0]
            data2 = temp[i][1]
            
            arr1 = np.asarray( data1.events )
            arr2 = np.asarray( data2.events )
            
            try:
                data1Arr = arr1.reshape( data1.event_count, -1 )
                data2Arr = arr2.reshape( data2.event_count, -1 )
                arrBoth = np.concatenate( [data1Arr, data2Arr], axis = 1)
                self.listArrBoth.append( arrBoth )
                self.listArr1.append(data1Arr)
                self.listArr2.append( data2Arr )
                self.listFlowData1.append(data1)
                self.listFlowData2.append(data2)
                self.output.append(data1.name)            
            except:
                continue
            
            
            
    
    
    def save_single( self ) :
        
        #require runnig single file reading function first #
        dataDF = self.store[0]
        dataDF1 = self.store[1]
        dataDF2 = self.store[2]
        datafcs1 = self.store[3]
        datafcs2 = self.store[4]
        name_ = self.store[5]
        
        dataDF = pd.DataFrame(dataDF)
        dataDF1 = pd.DataFrame(dataDF1)        
        dataDF2 = pd.DataFrame(dataDF2)
        
        dataDF.to_csv(f"{self.OUTsingle}/{name_}_DataFrame_.csv")
        dataDF1.to_csv(f"{self.OUTsingle}/{name_}_DataFrame_1_.csv")        
        dataDF2.to_csv(f"{self.OUTsingle}/{name_}_DataFrame_2_.csv")
        
        datafcs1.write_fcs(f'{self.OUTsingle}/{name_}_unit16_.fcs')
        datafcs2.write_fcs(f'{self.OUTsingle}/{name_}_unit32_.fcs')
        
        print(f"\n All the output from this Func is now present in {self.OUTsingle} \n")
        time.sleep(2)
        return
    
    
    def save_all( self ) :
        
        nh = randint(1234)
        
        for i in range( len(self.listArrBoth) ) :
            
            tempData = self.listArrBoth[i]
            tempdata1 = self.listArr1[i]
            tempdata2 = self.listArr2[i]
            tempfcs_1 = self.listFlowData1[i]
            tempfcs_2 = self.listFlowData2[i]
            tempName = self.output[i]
            
            tempData = pd.DataFrame(tempData)
            tempdata1 = pd.DataFrame(tempdata1)
            tempdata2 = pd.DataFrame(tempdata2)
            
            tempData.to_csv(f"{self.OUTcsv}/{tempName}__idhash{nh}__DataFrame.csv")
            tempdata1.to_csv(f"{self.OtherCSV}/{tempName}__idhash{nh}__DataFrame_1_.csv")            
            tempdata2.to_csv(f"{self.OtherCSV}/{tempName}__idhash{nh}__DataFrame_2_.csv")            
            
            tempfcs_1.write_fcs(f'{self.OUTfcs}/{tempName}_unit16_.fcs')
            tempfcs_2.write_fcs(f'{self.OUTfcs}/{tempName}_unit32_.fcs')           
        
        print(f"\n All the output from this Func is now present in {self.OUTsingle} \n")
        time.sleep(2)
        return
    
    def draw(self, label = None):
        
        if label:
            label_ = label
        else:
            temp = re.search(r'normal', self.inputFolder)
            if temp != None:
                label_ = 'Normal'
            else:
                label_ = 'Seek'
        
        plt.figure(figsize=(8, 6))
        
        for i in range( len(self.listArrBoth) ) :
            
            temp = self.listArrBoth[i]
            for j in range( ((temp.shape[1]) - 2) ) :
                
                plt.scatter( temp[:,j], temp[:,j+1] , cmap='viridis', s = 3 )
            
            plt.xlim(0, 1025)
            plt.ylim(0, 1025)
            plt.xlabel('FSLis')
            plt.ylabel('SSLin')
            plt.title(label_)
            plt.legend()
            #plt.colorbar(label='Color')
            #plt.grid(True)
            plt.savefig(f"{self.OUTfig}/{randint(1234)}.jpg")
            plt.show()
            
    
    
    def main(self) :
        
        print( " \n \n   !.!.!.>  Please Ignore The warnings  <.!.!.!.\n \n ")
        self.get_data()
        self.read_data()
        self.save_all()
        print('done')
        time.sleep(2)
        self.draw()
