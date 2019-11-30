#machine problem 3
import numpy as np

def bestfit(n):
    
    nx = n[:,0]
    ny = n[:,1]
    
    #1st degree
    p1 = np.polyfit(nx, ny, 1)
    y1 = np.polyval(p1, nx)
    e1 = ny - y1
    error1 = np.linalg.norm(e1)
    
    #2nd degree 
    p2 = np.polyfit(nx, ny, 2)
    y2 = np.polyval(p2, nx)
    e2 = ny - y2
    error2 = np.linalg.norm(e2)
    
    #3rd degree 
    p3 = np.polyfit(nx, ny, 3)
    y3 = np.polyval(p3, nx)
    e3 = ny - y3
    error3 = np.linalg.norm(e3)
    
    #4th degree 
    p4 = np.polyfit(nx, ny, 4)
    y4 = np.polyval(p4, nx)
    e4 = ny - y4
    error4 = np.linalg.norm(e4)
    
    #5th degree 
    p5 = np.polyfit(nx, ny, 5)
    y5 = np.polyval(p5, nx)
    e5 = ny - y5
    error5 = np.linalg.norm(e5)
    
    #6th degree 
    p6 = np.polyfit(nx, ny, 6)
    y6 = np.polyval(p6, nx)
    e6 = ny - y6
    error6 = np.linalg.norm(e6)
    
    #7th degree 
    p7 = np.polyfit(nx, ny, 7)
    y7 = np.polyval(p7, nx)
    e7 = ny - y7
    error7 = np.linalg.norm(e7)
    
    #8th degree 
    p8 = np.polyfit(nx, ny, 8)
    y8 = np.polyval(p8, nx)
    e8 = ny - y8
    error8 = np.linalg.norm(e8)
    
    #9th degree 
    p9 = np.polyfit(nx, ny, 9)
    y9 = np.polyval(p9, nx)
    e9 = ny - y9
    error9 = np.linalg.norm(e9)
    
    #10th degree 
    p10 = np.polyfit(nx, ny, 10)
    y10 = np.polyval(p10, nx)
    e10 = ny - y10
    error10 = np.linalg.norm(e10)
    
    #getting the least norm of error vector
    error = min(error1, error2, error3, error4, error5, error6, error7, error8,
              error9, error10)
    
    if error == error1:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p1)
        
    elif error == error2:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p2)
        
    elif error == error3:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p3)
    
    elif error == error4:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p4)
        
    elif error == error5:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p5)
    
    elif error == error6:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p6)
    
    elif error == error7:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p7)
        
    elif error == error8:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p8)
        
    elif error == error9:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p9)
        
    elif error == error10:
        print ('The coefficients of the polynomial f(x) that would best approximate the data according to the least-norm error vector e(x) are: ')
        print (p10)
        
    else:
        return