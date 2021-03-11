import unittest
import Calculator
class test_Calculator(unittest.TestCase): 
	def test_Add(self):
                #Testing Actual Results
		result = Calculator.Add(0,0)
		self.assertEqual(result, 0)
		
		result = Calculator.Add(1,1)
		self.assertEqual(result, 2)
		
		result = Calculator.Add(4, 4)
		self.assertEqual(result, 8)


		result = Calculator.Add(20, 4)
		self.assertEqual(result, 24)

		result = Calculator.Add(-1, 4)
		self.assertEqual(result, 3)

		result = Calculator.Add(-1, -5)
		self.assertEqual(result, -6)
		result = Calculator.Add("stuff", "string")
		self.assertEqual(result, "Error")

		result = Calculator.Add([1,0], [1])
		self.assertEqual(result, "Error")

		
	def test_Sub(self):
                #Testing Actual Results
		result = Calculator.Sub(0,0)
		self.assertEqual(result, 0)
		
		result = Calculator.Sub(1,1)
		self.assertEqual(result, 0)
		
		result = Calculator.Sub(6, 5)
		self.assertEqual(result, 1)
		
                

		result = Calculator.Sub(20, 4)
		self.assertEqual(result, 16)

		result = Calculator.Sub(-1, 4)
		self.assertEqual(result, -5)
		result = Calculator.Sub(-1, -5)
		self.assertEqual(result, 4)

		result = Calculator.Sub("stuff", "string")
		self.assertEqual(result, "Error")

		result = Calculator.Sub([1,0], [1])
		self.assertEqual(result, "Error")

	def test_Mul(self):
		result = Calculator.Mul(0,0)
		self.assertEqual(result, 0)
		
		result = Calculator.Mul(1,1)
		self.assertEqual(result, 1)
		
		result = Calculator.Mul(6, 5)
		self.assertEqual(result, 30)



                
		
		result = Calculator.Mul(-1,4)
		self.assertEqual(result, -4)
		result = Calculator.Mul(20, 4)
		self.assertEqual(result, 80)
		result = Calculator.Mul(-1,-5)
		self.assertEqual(result, 5)
		result = Calculator.Mul("stuff", "string")
		self.assertEqual(result, "Error")

		result = Calculator.Mul([1,0], [1])
		self.assertEqual(result, "Error")


	def test_Div(self):
                #Testing Actual Results
		result = Calculator.Div(0,0)
		self.assertEqual(result, "Error")
		
		result = Calculator.Div(0,1)
		self.assertEqual(result, 0)


		result = Calculator.Div(4,8)
		self.assertEqual(result, 0.5)
		result = Calculator.Div(1,0)
		self.assertEqual(result, "Error")
		
		result = Calculator.Div(20,4)
		self.assertEqual(result, 5)
		result = Calculator.Div(10, 5)
		self.assertEqual(result, 2)
		result = Calculator.Div(-1, -4)
		self.assertEqual(result, 0.25)
		result = Calculator.Div(-1, 4)
		self.assertEqual(result, -0.25)
		result = Calculator.Div("stuff", "string")
		self.assertEqual(result, "Error")

		result = Calculator.Div([1,0], [1])
		self.assertEqual(result, "Error")
		


if __name__ == "__main__":
        unittest.main()
