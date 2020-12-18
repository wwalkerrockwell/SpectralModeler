from matplotlib import pyplot as plt
import splat
import splat.model as spmdl
import math
plt.matplotlib.use('Qt5Agg') #Important!

name = input("Enter the shortname of the desired spectra: ") #Take in user input
spectra = splat.getSpectrum(shortname=name) #0949+0806 is a good example
sp = spectra[0]
sp.plot() #Plot users spectra

#Uncomment these lines to compare models and fit models

#spmdl.modelFitGrid(sp)
#mdl = spmdl.loadModel(teff=2400,logg=5.0, Z=0.5, modelset='btsettl08')
#splat.compareSpectra(sp, mdl, plot = True)

plt.show()


#Take user input
starMass = float(input("Enter the Mass of the star (kg): "))
planetMass = float(input("Enter the mass of the planet (0 if unknown or incosenquential): "))
innerBound = float(input("Enter the inner boundary of the Habitable Zone (Meters): "))
outerBound = float(input("Enter the outer boundary of the Habitable Zone (Meters): "))
#Calculate and print periods
innerPeriod = math.sqrt((4.0*(3.141592**2))/((6.67e-11)*(starMass + planetMass)) * (innerBound**3))
innerPeriod = innerPeriod/(3.154e7)
outerPeriod = math.sqrt((4.0*(3.141592**2))/((6.67e-11)*(starMass + planetMass)) * (outerBound**3))
outerPeriod = outerPeriod/(3.154e7)
print("Inner Period = ", innerPeriod, "years.\nOuter Period = ", outerPeriod, "years")  
