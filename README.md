# File Format Converter

I deal with a ton of files in various formats on the daily, and opening a web converter everytime is slow and annoying. So I'm writing this tiny flask web app to do this all locally. 

### Structure
Output formats are stored in the formats_hub directory. Each format will get it's own little module. app.py combines it all into a single flask server. 

### How to use
Run the flask app. Upload your file, select the format. Can't be much simpler than that.

### Future Targets
- Dynamic list based on upload file format
- Copy to clipboard functionality
- Context Menu (TBD)
- ~~Add Video~~ ✅ Added Video
- Add More Formats
