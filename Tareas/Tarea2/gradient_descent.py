class Gradient():
    def __init__(self):
        pass
    def cost(self,theta0,theta1,x,y):
      #donde theta0 y theta1 son los parámetros a probar,
        #x y y son nparrays de la misma dimensión
        n=x.size
        #aqui podrian depurar que los tamaños de los arreglos sean iguales

        #calculo del costo en la variable J
        J=(1/(2*n))*np.sum(np.power(( (theta0+theta1*x)-(y) ),2)) #terminen ustedes... 
        time.sleep(1)
        return J
    """
    Función de theta0 que el entran los dos thetas, X y Y
    """
    def gradient_theta0(self,theta0,theta1,x,y):
        n=x.size# para normalizar el número de muestras
        return (1/n)*np.sum(( (theta0+theta1*x)-(y) ))
        """
        Función de theta1 que el entran los dos thetas, X y Y
        """
    def gradient_theta1(self,theta0,theta1,x,y):
        n = x.size# para normalizar el número de muestras
        return (1/n)*np.sum( ((theta0+theta1*x)-(y))*x )

    def gradient_descent(self, alpha, theta0, theta1, x, y):
        G0=self.gradient_theta0(theta0,theta1,x,y)
        G1=self.gradient_theta1(theta0,theta1,x,y)
        
        theta0km1=theta0-alpha*G0
        theta1km1=theta1-alpha*G1
        return theta0km1,theta1km1