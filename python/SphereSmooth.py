import math

def main():
    phi = 0 #180
    theta = 0 #360
    
    Vertices = [[]]
    i = 0
    #set up all vertices
    for phi in range(0,180,(180//16)):
        Vertices.append([])
        for theta in range(0,360,(360//32)):
            Vertices[i].append(
                (math.sin(math.radians(phi))*math.cos(math.radians(theta)),
                math.cos(math.radians(phi)),
                math.sin(math.radians(phi))*math.sin(math.radians(theta))))
            
        
        print(Vertices[i])   
        print("the length of vertices ring is:",len(Vertices[i]))   
        
        i+=1
        print(phi)
    phi = 180
    for theta in range(0,360,(360//32)):
        Vertices[i].append(
            (math.sin(math.radians(phi))*math.cos(math.radians(theta)),
            math.cos(math.radians(phi)),
            math.sin(math.radians(phi))*math.sin(math.radians(theta))))        
    print("the last line of vertices are: \n", Vertices[len(Vertices)-1])
    print("the length of all vertices in one ring is:",len(Vertices),
          "\n",
          "and the length of each ring is:", len(Vertices[0]))
    
    #set up the faces
    #face on the upper pole
    UpperFaces = []
    
    for i in range(len(Vertices[0]),2,-1):
        UpperFaces.append((i-1,1,i))
        
    UpperFaces.append((len(Vertices[0]),1,2))
    print(UpperFaces)
    
    #face on the lower pole
    LowerFaces = []
    MaxValue = (len(Vertices)-2)*(len(Vertices[0])-1)+2 #514
    for i in range(MaxValue-1,MaxValue-32,-1):
        LowerFaces.append((i,MaxValue,i-1))
        
    LowerFaces.append((MaxValue-32,
                       MaxValue, 
                        MaxValue-1))
    print(LowerFaces)
    print("the max value is",MaxValue)
    #middle faces
    middleFaces = []
    for i in range(2,MaxValue-(len(Vertices)-1)*2-2,len(Vertices[0])-1):
        
        for j in range(i+len(Vertices[0])-2,i,-1):
            
            middleFaces.append((j,
                                j+len(Vertices[0])-2,
                                j-1))#add upper face
            middleFaces.append((j,
                                j+len(Vertices[0])-1,
                                j+len(Vertices[0])-2))#add lower face
        #add last face
        print("i is",i)
        middleFaces.append((i+len(Vertices[0])-1,i+len(Vertices[0])-2,i))#upper last
        middleFaces.append((i+len(Vertices[0])-1,i+(len(Vertices[0])-1)*2-1,i+len(Vertices[0])-2))#lower last
    #upper middle faces
    
    #lower middle faces

    f = open("SphereSmooth.obj","w+")
    #the first center point
    f.write("v %f %f %f\n" % (Vertices[0][0][0],Vertices[0][0][1],Vertices[0][0][2]))
    for j in range(1,len(Vertices)-1):
        for k in range(len(Vertices[j])-1):
            f.write("v %f %f %f\n" % (Vertices[j][k][0],Vertices[j][k][1],Vertices[j][k][2]))
    #the otherside of the center point
    f.write("v %f %f %f\n" % (Vertices[len(Vertices)-1][0][0],
                              Vertices[len(Vertices)-1][0][1],
                              Vertices[len(Vertices)-1][0][2]))
    
    #add normal for vertices
    f.write("vn %f %f %f\n" % (Vertices[0][0][0],Vertices[0][0][1],Vertices[0][0][2]))
    for j in range(1,len(Vertices)-1):
        for k in range(len(Vertices[j])-1):
            f.write("vn %f %f %f\n" % (Vertices[j][k][0],Vertices[j][k][1],Vertices[j][k][2]))
            
    #the otherside of the center point
    f.write("vn %f %f %f\n" % (Vertices[len(Vertices)-1][0][0],
                              Vertices[len(Vertices)-1][0][1],
                              Vertices[len(Vertices)-1][0][2]))    
    
    for j in range(len(UpperFaces)):
        f.write("f %d//%d %d//%d %d//%d\n" % (UpperFaces[j][0],UpperFaces[j][0],UpperFaces[j][1],UpperFaces[j][1],UpperFaces[j][2],UpperFaces[j][2]))

    for j in range(len(LowerFaces)):#for i in range will not include the last one
        #so it is safe to use len(list) to iterate
        f.write("f  %d//%d %d//%d %d//%d\n" % (LowerFaces[j][0],LowerFaces[j][0],LowerFaces[j][1],LowerFaces[j][1],LowerFaces[j][2],LowerFaces[j][2]))
    
    for j in range(len(middleFaces)):
        f.write("f  %d//%d %d//%d %d//%d\n" % (middleFaces[j][0],middleFaces[j][0],middleFaces[j][1],middleFaces[j][1],middleFaces[j][2],middleFaces[j][2]))
    f.close()