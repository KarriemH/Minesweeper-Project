import settings 

def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_prct(percentage):
    return (settings.WIDTH / 100) * percentage

print (height_prct(50))
print (width_prct(50))