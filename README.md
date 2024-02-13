@Kritim Bastola

Here are the extensions for QGIS

Create New Species File
This function is intended to allow the user to create a single vector data layer which is based on the templates provided in the Templates folder of the QGIS Toolbox Design Google Drive folder.
 User Inputs (all required)
OutputLocation - Output location (directory, geodatabase, or geopackage)
SciName - Scientific name (can be in one of three formats “Genus species”, “Genus species subsp. subspecies”, or “Genus species var. variety”)
FeatureType - Feature type (Point or Polygon)
Processing
This can all be done using the EXPORT function
Required inputs:
Vector layer from EXPORT templates (included in Google Drive folder)
For shapefiles with point geometry, we will always use pointTemplate_with_optional_attributes_2021_05
For shapefiles with polygon geometry use polygonTemplate_2021_05
Geodatabases will use templates_gdb_2021_05
For geopackages, an option is available in the EXPORT function to save a shapefile as a geopackage layer. In this case the relevant shapefile template for the appropriate geometry type (point or polygon) can be exported as a geopackage. If an existing geopackage has been selected, a new feature layer can be generated using the EXPORT function. If a directory has been selected, create a new geopackage
File Name
If a directory has been selected for a geodatabase or geopackage creation (as opposed to a geopackage or geodatabase) give a generic name to it (e.g. “New_GeoDatabase”)
If a geodatabase or geopackage has been selected in OutputLocation, filename need not be specified. Only the layer name is required.
For shapefiles this will be named based on scientific name input (SciName)
Remove punctuation (e.g. “var.” -> “var”)
Replace all spaces with underscores
Feature layer to be named based on scientific name input (SciName)
Remove punctuation (e.g. “var.” -> “var”)
Replace all spaces with underscores
CRS
Always EPSG: 4326 – WGS 84
Geometry Type
Based on FeatureType

Create multiple shapefiles, feature classes, or geopackage layers from list
This function will create a set of feature classes (shapefiles, geodatabase features, or geopackage layers) based on a list of species provided by the user in a standardized format. The format is a .csv file is based on a file which can be exported directly from the IUCN Red List database software. It’s a standardized document with standardized fields.
User Inputs
VectorType - Shapefile, Geodatabase, Geopackage
SpeciesList - .csv file (based on taxonomy.csv template)
OutputLocation - output location (folder, geodatabase, or geopackage)
FeatureType - geometry type (points, or polygons)
Processing
Build column for scientific name (OutputTitle)
If infraType is blank, create species name
Value in column “genus”, underscore, value in column “species”
If infraType is not blank, create infraspecies name
Value in column “genus”, underscore, value in column “species”, underscore, value in column “infraType, underscore, value in column “infra_name”
If VectorType = Shapefile
EXPORT template file matching geometry type with titles OutputTitle (one for each row in SpeciesList)
If VectorType = Geodatabase
Export geodatabase template and populate with one feature class of the corresponding geometry type (FeatureType) with the name OutputTitle
If VectorType = Geopackage
Export geopackage template and populate with one layer of the corresponding geometry type (FeatureType) with the name OutputTitle

Add Attribute Files

Given a point or polygon file, check to determine whether the necessary attribute fields are present and, add any required attribute fields which are missing.

User Inputs
InputVector - Shapefile, feature class (from geodatabase), or layer (from geopackage)
GeometryType - Point or polygon

Processing
Check if fields with the 26 required titles are present (copy process from Check Fields below)
Check to determine if 26 required fields have the correct field type (integer, string, boolean, etc.) (copy process from Check Fields below)
If fields are missing, add them
If fields have the wrong type, create a copy with the correct field type
If a field with the title “binomial” is present, copy this field into the newly created “sci_name” field
If field “event_year” is missing, but a field titled “year” or “year_” is present, generate “event_year” and populate the field with values from “year” or “year_”

Fill Fields

Fill fields for all rows with the user specified values. User input must have same titles and field types in user input file as are present in template file.

User Inputs
FeatureFile (required) - a shapefile, geodatabase feature class, or geopackage layer
SciName (optional) - string
PresenceField (optional) - short integer
OriginField (optional) - short integer
CompilerField (optional) - string
YrCompiled (optional) - short integer
CitationField (optional) - string
DataSensitive (optional) - boolean (TRUE or FALSE)

Processing
Check to determine if relevant fields (as specified in User Inputs) are present in FeatureFile
If not return error
If fields are present, use FIELD CALCULATOR to input user inputs into all rows according to field name


Check Fields

Given a point or polygon file, check to determine whether the necessary attribute fields are present and if necessary data is included. Return a response indicating what needs to be filled.

User Inputs
InputVector - Shapefile, feature class (from geodatabase), or layer (from geopackage)

Processing
Determine geometry type for InputVector (point or polygon)
If Point, compare fields and field types against point template (not including expanded fields)
If Polygon, compare field types against polygon template
Check to determine if all required fields contain data for each row (both points and polygons)
SciName
Presence
Origin
Compiler
YrCompiled
DataSens
For points files
Spatialref (all rows should be identical)
Dec_lat (not NULL, <= 90, >=-90)
Dec_long (not NULL, <=180, >=-180)
For polygon files
CHECK VALIDITY
If errors returned FIX GEOMETRIES
Repair method is “Structure”
Return warning for fields which are not complete or have data incompatible with the type

Split layer by attribute

Splits input layer into multiple layers based on attribute values.

User Inputs (all required)
FeatureLayer - shapefile, geodatabase feature class, or geopackage layer
SplitAttribute - dropdown list of attributes including (sci_name)
OutputLocation - file, geodatabase, or geopackage layer

Processing
SpeciesList <- LIST UNIQUE VALUES in field SplitAttribute from FeatureLayer
For each in SpeciesList, SELECT BY ATTRIBUTE (select SpeciesList[i] from FeatureLayer attribute SplitAttribute)
EXPORT FeatureLayer to location OutputLocation
Selected values only
Give title SpeciesList[i] with spaces replaced by underscores
If NULL included in SpeciesList, export all rows containing NULL to binomial_isNULL.shp

Refine Species to Coastline

Clip user input file to coastline shapefile.

User Inputs (all required)
UserLayer - shapefile, geodatabase feature class, geopackage layer
OutputLocation - file, geodatabase, geopackage
DistType - marine or terrestrial

Processing
Determine CRS of UserLayer
If UserLayer CRS =/= WGS84 (EPSG4326) REPROJECT LAYER
Input layer = UserLayer
Target CRS = WGS84 (EPSG4326)
Reprojected output -> create temporary layer ->ReprojectedLayer
If ReprojectedLayer exists
If DistType = terrestrial
CLIP
Input layer = ReprojectedLayer
Overlay layer = Land_Masses_and_Ocean_Islands (from templates folder)
Output Location = OutputLocation
If DistType = marine
DIFFERENCE
Input layer = ReprojectedLayer
Overlay layer = Land_Masses_and_Ocean_Islands (from templates folder)
Output Location = OutputLocation
If ReprojectedLayer does not exist
If DistType = terrestrial
CLIP
Input layer = UserLayer
Overlay layer = Land_Masses_and_Ocean_Islands (from templates folder)
Output Location = OutputLocation
If DistType = marine
DIFFERENCE
Input layer = UserLayer
Overlay layer = Land_Masses_and_Ocean_Islands (from templates folder)
Output Location = OutputLocation

Calculate Extent of Occurrence

Calculates the area of the minimum convex polygon surrounding a point or polygon file. A warning will need to be given explaining that the tool will not function properly for species with ranges that cross the international dateline, or extend over one of the poles. In these cases, more advanced methods for determining the EOO should be used. Input layer must be formatted for submission to the IUCN Red List (including fields for Presence, Origin, and sci_name).

User Inputs:
UserLayer - shapefile, geodatabase feature class, geopackage layer

Processing
Set project units to kilometers (I do not know how to do this using processing toolbox)
Determine CRS of UserLayer
If UserLayer CRS =/= World Cylindrical Equal Area (ESRI:54034) REPROJECT LAYER
Input layer = UserLayer
Target CRS = World Cylindrical Equal Area (ESRI:54034)
Reprojected output -> create temporary layer -> EqualAreaLayer
Else EXPORT UserLayer ->create temporary layer -> EqualAreaLayer
Subset features of interest
SELECT BY EXPRESSION
Input layer = EqualAreaLayer
Expression = “presence=1 AND origin in (1,2,6)”
Matching Features exported to temporary layer “EOO_temp”
Draw minimum convex polygon
MINIMUM BOUNDING GEOMETRY
Input layer = EOO_temp
Field (leave blank)
Geometry Type = Convex Hull
Create temporary layer -> EOO_hull
Calculate Area
FIELD CALCULATOR
Input layer = EOO_hull
Field Name = EOO
Result field type = double
Return result to user

Calculate Area of Occupancy

