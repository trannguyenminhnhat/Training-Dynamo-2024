import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
uiDoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

class SelectionFilter(ISelectionFilter):
	def __init__(self, ctgName1 , ctgName2):
		self.ctgName1 = ctgName1
		self.ctgName2 = ctgName2

	def AllowElement(self, element):
		if element.Category.Name == self.ctgName1 or element.Category.Name == self.ctgName2:
			return True
		else:
			return False
	def AllowReference(ref, xyZ):
		return False

selectionFilter = SelectionFilter("Walls", "Structural Columns")
selectedElements = uiDoc.Selection.PickElementsByRectangle(selectionFilter, "Select elements")

columns = []
walls = []
for element in selectedElements:
    if element.Category.Name == "Structural Columns":
        columns.append(element)
    elif element.Category.Name == "Walls":
        walls.append(element)

OUT = (columns, walls)
