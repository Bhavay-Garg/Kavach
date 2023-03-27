from bs4 import BeautifulSoup
import os

k=0
for root, dirs, files in os.walk(r'D:/Kavach/Dataset'):
    for file in files:
        # check the extension of files
        if file.endswith('.xml'):
            # print whole path of files
            path=os.path.join(root, file)

            # process each xml
            with open(path, 'r') as f:
                data = f.read()


            Bs_data = BeautifulSoup(data, "xml")

            x_min = Bs_data.find_all('xmin')
            y_min = Bs_data.find_all('ymin')
            x_max = Bs_data.find_all('xmax')
            y_max = Bs_data.find_all('ymax')
            ih=Bs_data.find_all('height')
            iw=Bs_data.find_all('width')

            x_min=int(str(x_min)[7:-8])
            x_max=int(str(x_max)[7:-8])
            y_min=int(str(y_min)[7:-8])
            y_max=int(str(y_max)[7:-8])
            ih=int(str(ih)[9:-10])
            iw=int(str(iw)[8:-9])


            x=((x_min+x_max)/2)/iw
            y=((y_min+y_max)/2)/ih
            h=(y_max-y_min)/ih
            w=(x_max-x_min)/iw

            t=open(os.path.join(root,file[:-4]+".txt"),"w")
            t.write("0 "+str(x)+" "+str(y)+" "+str(w)+" "+ str(h))
            t.close()
            k+=1
            print(k, "files done")
            
