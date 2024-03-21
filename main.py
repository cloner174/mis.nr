#    #  #                       #         In the name of God   #    #
#
#github.com/cloner174
#cloner174.org@gmail.com
#
from flowio import read_multiple_data_sets
from os.path import exists
import flowkit as fk
import pandas as pd
import time
import os
import re


class nr:
    def __init__(self, input_folder, output_folder) :
        self.input = []
        self.names = []
        self.listFlowData1 = []
        self.listFlowData2 = []
        self.inputFolder = input_folder
        self.folderFiles = os.listdir(input_folder)
        print("\n Detecting the folders and subfolders... \n ")
        time.sleep(2)
        if exists( f"{output_folder}/CSVs/" ):
            print("\n CSVs folder already exists in output folder. cheking next require folder.. \n ")
            time.sleep(1)
        else:
            print(" Please Create a folder with name:: CSVs  inside the output folder ")
        if exists( f"{output_folder}/FCSs/" ) :
            print("\n FCSs folder already exists in output folder. cheking next require folder.. \n ")
            time.sleep(1)
        else:
            print(" Please Create a folder with name:: FCSs  inside the output folder ")
        print( "\n All Done ! \n ")
        time.sleep(1)
        print("\n Finishing up .... \n ")
        time.sleep(2)
        self.OUTcsv = f"{output_folder}/CSVs/"
        self.OUTfcs = f"{output_folder}/FCSs/"
        print( "\n Secssusfully Create The Object. \n ") 
        time.sleep(1)
        print("\n Now you may use any of Functions from this class! \n ")
        time.sleep(1)
    def get_data(self):
        for anyFile in self.folderFiles:
            if anyFile.lower().endswith('.lmd'):
                self.input.append( os.path.join(self.inputFolder, anyFile) )
        return
    def read_data(self) :
        temp = []
        for file in self.input :
            temp.append( read_multiple_data_sets(file, ignore_offset_error=True) )
        for i in range( len( temp )) :    
            data1 =  temp[i][0]
            data2 = temp[i][1]
            self.listFlowData1.append(data1)
            self.listFlowData2.append(data2)
            self.names.append(data1.name)
            data1.write_fcs(f'{self.OUTfcs}/{data1.name}_unit16_.fcs')
            data2.write_fcs(f'{self.OUTfcs}/{data1.name}_unit32_.fcs')
        return
    def save_all( self ) :
        for i in range( len(self.listFlowData1) ) :
            tempfcs_1 = fk.Sample(self.listFlowData1[i])
            tempfcs_2 = fk.Sample(self.listFlowData2[i])
            tempName = self.names[i]
            tempcsv_1 = tempfcs_1.as_dataframe(source='raw')
            tempcsv_2 = tempfcs_2.as_dataframe(source='raw')
            tempBoth = pd.concat([tempcsv_1,tempcsv_2],axis=1)
            tempBoth.to_csv(f'{self.OUTcsv}/{tempName}_DataFrame_.csv')
        print(f"\n All the output from this Func is now present in {self.OUTcsv} \n")
        time.sleep(2)
        return
    def draw(self, label = None):
        laybel = []
        DaTa16 = []
        DaTa32 = []
        names = []
        for i in range( len(self.listFlowData1) ) :
            name_ = self.names[i]
            tempfcs16 = (self.listFlowData1[i])
            tempfcs32 = (self.listFlowData2[i])
            DaTa16.append(tempfcs16)
            DaTa32.append(tempfcs32)
            names.append(name_)
            if label:
                laybel.append(label)
            else:
                tempNorm = re.search(r'normal', self.inputFolder)
                tempSeek = re.search(r'hum', self.inputFolder)
                if tempNorm != None:
                    laybel.append('Normal')
                elif tempSeek != None:
                    laybel.append('Seek')
                else:
                    laybel.append(name_)
        return DaTa16, DaTa32, names, laybel
    def main(self) :
        print( " \n \n   !.!.!.>  Please Ignore The warnings  <.!.!.!.\n \n ")
        time.sleep(2)
        self.get_data()
        self.read_data()
        self.save_all()
        return self.draw()
#end#