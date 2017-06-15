def epsg(crs):
    crs = str(crs)  # force crs to string

    # Define needed CRS here
    custom_crs = {
        # RI State Plane 1983
        '3438': {'proj': 'tmerc',
                 'lat_0': '41.08333333333334',
                 'lon_0': '-71.5',
                 'k': '0.99999375',
                 'x_0': '100000',
                 'y_0': '0',
                 'datum': 'NAD83',
                 'units': 'us-ft'},
    }

    # find the crs in the dict, or pass through
    keys = set(custom_crs.keys())
    if crs in keys:
        return custom_crs.get(crs)
    else:
        return {'init': 'epsg:' + crs}
