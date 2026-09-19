try:
	from .base.XYZ import Third
except ImportError:
	from base.XYZ import Third


if __name__ == "__main__":
	instance = Third()
	print(Third.__mro__)
	print(instance.name())
	print(instance.sirname())