SELECT hospcode, hospname, zone, cmi 
FROM cmi 
WHERE hospcode in %(hospcode)s