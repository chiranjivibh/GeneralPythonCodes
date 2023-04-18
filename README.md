# GeneralPythonCodes
Config files for my GitHub profile.
In this project I am archiving my test python codes which can be easily find on google search, suggestions and modifications 

I used different sites to copy codes and test by myself to familiarize my self and can be usefull in future. 

Use anaconda for installing PYHDF, which is very usefull for installing SD and SDF 


conda install -c conda-forge pyhdf
conda install -c conda-forge cartopy



def Retrive_Point_source_Modis(dirlist1,Data_field,logn):
    n = 0
    for i in dirlist1:
        f = SD(i,SDC.READ)
        lat = f.select('Latitude')
        lon = f.select("Longitude")
        data2D = f.select(Data_field)
        latitude = lat[:,:]
        lognitude = lon[:,:]
        data = data2D[:,:].astype(np.double)
        data [data<-9000.0] = 0.0
    #     latitude[latitude<-900]  = 90 #np.nanmean(latitude[latitude<-900])
    #     lognitude[lognitude <-900]  = 21 #np.nanmean(lognitude[lognitude<-90])
        if n ==0:
            lognitude1 = lognitude
            lattitude1 = latitude
            data1 = data
        else:
            lognitude1 = np.vstack((lognitude1,lognitude))
            lattitude1 = np.vstack((lattitude1,latitude))
            data1 = np.vstack((data1,data))
        n+=1
    # find nearby lattitude and lonitude from the grid,
    long_s = np.sort(lognitude1[lognitude1>logn])[0]
    print( abs(logn-long_s) )
    return data1[lognitude1==long_s][0],lognitude1[lognitude1==long_s][0],lattitude1[lognitude1==long_s][0]

Retrive_Point_source_Modis(dirlist,Data_field,27.555),Retrive_Point_source_Modis(dirlist,Data_field,27.1),Retrive_Point_source_Modis(dirlist,Data_field,27.555)
