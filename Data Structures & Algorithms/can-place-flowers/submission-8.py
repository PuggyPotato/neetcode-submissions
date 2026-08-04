class Solution:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		if n == 0:
			return True

		if len(flowerbed) < 2:
			if flowerbed[0] == 0 and n <= 1:
				return True
		
		for i in range(len(flowerbed)):
			if i == 0:
				if flowerbed[i] == 0 and flowerbed[i+1] == 0:
					flowerbed[i] = 1
					n-=1	
			elif i == len(flowerbed) - 1:
				if flowerbed[i] == 0 and flowerbed[i-1] == 0:
					flowerbed[i] = 1
					n-=1
			else:
				if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
					flowerbed[i] = 1
					n-=1
		print(flowerbed)
		return n <= 0