# QGIS Extensions for Biodiversity Conservation

This document outlines several QGIS extensions developed to assist in biodiversity conservation efforts, including the creation of species files, managing attribute files, and performing specific analyses like calculating the extent of occurrence (EOO) and area of occupancy (AOO). These tools are designed to streamline the process of managing and analyzing spatial data related to species distribution and conservation status.

## 1. Create New Species File

### Purpose
To generate a single vector data layer for a new species based on predefined templates.

### User Inputs
- **OutputLocation**: Directory, geodatabase, or geopackage where the new file will be saved.
- **SciName**: Scientific name of the species.
- **FeatureType**: Geometry type (Point or Polygon).

### Processing Steps
- Utilize the EXPORT function with the appropriate template based on the feature type and output format.
- Name the feature layer based on the scientific name, removing punctuation and replacing spaces with underscores.
- Set the Coordinate Reference System (CRS) to EPSG:4326 (WGS 84).

## 2. Create Multiple Shapefiles, Feature Classes, or Geopackage Layers

### Purpose
To generate multiple feature classes based on a list of species provided in a .csv format.

### User Inputs
- **VectorType**: Shapefile, Geodatabase, or Geopackage.
- **SpeciesList**: Path to the .csv file containing species information.
- **OutputLocation**: Where to save the generated files.
- **FeatureType**: Geometry type (Points or Polygons).

### Processing Steps
- Build scientific names for species or infraspecies based on the .csv data.
- Export data using the appropriate template for the specified vector type and geometry.

## 3. Add Attribute Files

### Purpose
To check for missing attribute fields in a vector file and add them as necessary.

### User Inputs
- **InputVector**: Shapefile, geodatabase feature class, or geopackage layer.
- **GeometryType**: Point or polygon.

### Processing Steps
- Verify the presence of 26 required fields and their types.
- Add missing fields or adjust field types as needed.
- Special handling for fields like "binomial" and "event_year".

## 4. Fill Fields

### Purpose
To populate fields in a vector file based on user input.

### User Inputs
- **FeatureFile**: The file to be updated.
- **SciName, PresenceField, OriginField, CompilerField, YrCompiled, CitationField, DataSensitive**: Fields to be filled.

### Processing Steps
- Check for the presence of specified fields.
- Use FIELD CALCULATOR to populate fields.

## 5. Check Fields

### Purpose
To verify the presence of necessary attribute fields and data within a vector file.

### User Inputs
- **InputVector**: Shapefile, geodatabase feature class, or geopackage layer.

### Processing Steps
- Determine geometry type and compare against templates.
- Verify data completeness in required fields.

## 6. Split Layer by Attribute

### Purpose
To divide a layer into multiple layers based on attribute values.

### User Inputs
- **FeatureLayer**: The input vector file.
- **SplitAttribute**: Attribute to split by.
- **OutputLocation**: Where to save the split layers.

### Processing Steps
- List unique values in the specified attribute.
- Export subsets of the layer based on these unique values.

## 7. Refine Species to Coastline

### Purpose
To clip a species distribution layer to coastline boundaries.

### User Inputs
- **UserLayer**: Input vector file.
- **OutputLocation**: Where to save the clipped file.
- **DistType**: Marine or terrestrial.

### Processing Steps
- Reproject the input layer if necessary.
- Clip or difference the layer with coastline data based on the specified distribution type.

## 8. Calculate Extent of Occurrence (EOO)

### Purpose
To calculate the area of the minimum convex polygon that can contain all occurrences of a species.

### User Inputs
- **UserLayer**: Input vector file.

### Processing Steps
- Reproject the layer to a suitable CRS for area calculation.
- Select features based on presence and origin criteria.
- Calculate the area of the convex hull enclosing the selected features.

## 9. Calculate Area of Occupancy (AOO)

This section will detail the process for calculating the AOO, similar to the EOO calculation but focusing on the occupied area within the species' range.

---

For each extension, ensure you have the necessary QGIS version and plugins installed. Detailed instructions for each process, including required templates and example .csv formats, are available in the QGIS Toolbox Design Google Drive folder referenced in the user input sections.
