class _Shape:
  
  
    """
    Questa classe rappresenta una figura geometrica
    """
    
    def __init__(self, l):
        self._l = l

    
    def area(self):
        
        """
        Calcolo dell'area della figura
        """
        
        return
  
  
    def perimeter(self):
        
        """
        Calcolo del perimetro della figura
        """
        
        return
  
  
    def __repr__(self):
        
        """
        Stampiamo area e perimetro della figura
        """
        
        info = "Area della figura: %2.f" % self.area()
        info+="\nPerimetro della figura: %2.f" % self.perimeter()
        return info




class Triangle(_Shape):
    
    """
    Questa classe rappresenta un triangolo
    """

    def area(self):
        
        """
        Calcolo dell'area del triangolo
        """
        
        return self._l[0]*self._l[3]/2.
  
  
    def perimeter(self):
        
        """
        Calcolo del perimetro del triangolo
        """
        
        return self._l[0]+self._l[1]+self._l[2]




class Square(_Shape):
    
    """
    Questa classe rappresenta un quadrato
    """

    def area(self):
        
        """
        Calcolo dell'area del quadrato
        """
        
        return self._l*self._l
  
  
    def perimeter(self):
        
        """
        Calcolo del perimetro del triangolo
        """
        
        return self._l*4



class Rectangle(_Shape):
    
    """
    Questa classe rappresenta un quadrato
    """

    def area(self):
        
        """
        Calcolo dell'area del quadrato
        """
        
        return (self._l[0]+self._l[1])*2
  
  
    def perimeter(self):
        
        """
        Calcolo del perimetro del triangolo
        """
        
        return self._l[0]*self._l[1]
