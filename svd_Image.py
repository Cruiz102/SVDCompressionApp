
import numpy as np
from PIL import Image


class SVDImage():
    def __init__(self, filename):
        self.filename = filename
        self.singularValuesLength = 0
        self.SVDArrays = self.LoadSVD(self.filename)
        self.progressCounter = 0

    def LoadSVD(self,file):
        im = Image.open(file)
        r,g,b = Image.Image.split(im)
        r_data = np.asarray(r)
        g_data = np.asarray(g)
        b_data = np.asarray(b)
        r_s,r_v,r_d = np.linalg.svd(r_data)
        g_s,g_v,g_d = np.linalg.svd(g_data)
        b_s,b_v,b_d = np.linalg.svd(b_data)
        R_SVD = [r_s,r_v,r_d]
        G_SVD = [g_s,g_v,g_d]
        B_SVD = [b_s,b_v,b_d]
        self.singularValuesLength = len(r_v)
        return (R_SVD,G_SVD,B_SVD)

    def RankImageArray(self,arrays, rank): 
        U = arrays[0]
        S = arrays[1]
        Vh = arrays[2]
        rankImageArray = np.zeros((U.shape[0], Vh.shape[0]))
        Uh = U.transpose()
        for i in range(rank):
            rankImageArray +=  S[i]* np.outer(Uh[i],Vh[i])
            self.progressCounter += 1
        return rankImageArray

    def RankImageSVD(self, rank):
        r_ImageArray = self.RankImageArray(self.SVDArrays[0],rank)
        g_ImageArray = self.RankImageArray(self.SVDArrays[1],rank)
        b_ImageArray = self.RankImageArray(self.SVDArrays[2],rank)
        r_image = Image.fromarray(r_ImageArray).convert('L')
        g_image  = Image.fromarray(g_ImageArray).convert('L')
        b_image = Image.fromarray(b_ImageArray).convert('L')
        CompleteImage = Image.merge('RGB', (r_image, g_image, b_image))
        return CompleteImage





    
