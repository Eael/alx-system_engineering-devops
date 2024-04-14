# POST MORTEM REPORT APACHE SERVING ERROR CODE 500
## SUMMARY
- Problem Start Time : `GMT 18:01`
- Problem End Time : `GMT 21:12`
- Impact : `Server stopped serving webpage during the outage`
- Cause : `Error in configuration file`

## TIMELINE
- Issue was at GMT 18:01
- Issue was detected through user complaint
- Strace was used to log the apache service
- Error was thought to be incorrect naming of files
- Incident was escalated to the SE on site
- Issue was resolved by renaming mistake in config file


