# Importing necessary libraries
import clr
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, ElementCategoryFilter

# Getting the current Revit document and view
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
current_view = uidoc.ActiveView

# Creating a filter to get all columns in the current view
column_filter = ElementCategoryFilter(BuiltInCategory.OST_Structural_Column)

# Collecting all columns in the current view
columns_in_view = FilteredElementCollector(doc, current_view.Id).WherePasses(column_filter).ToElements()

# Output the results
OUT = [column.ToDSType(True) for column in columns_in_view]