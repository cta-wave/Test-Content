# Test-Content

This page collects information around CTA WAVE Test Content.

CTA WAVE Test Content is hosted here: https://cta-wave.github.io/Test-Content/


How to add content:
* Original Content: Submit an [issue](https://github.com/cta-wave/Test-Content/issues/new&labels=proposed-original)
* Proposed CTA WAVE Content: Submit an [issue](https://github.com/cta-wave/Test-Content/issues/new&labels=proposed-wave-content) 

## How does this site work

This website is a SPA coded using Vue.js and PureCSS, it relies on a flat file json database you can find [here](https://cta-wave.github.io/Test-Content/database.json)

The database is an object containing attributes discribing each asset.

Each asset has its own idea, generated from the content matrix, and its main type, and the object contains the representations, and how the content was generated.

```
{
    "CFHD" : {
        "./output/avc_sets/15_30_60/t1": {
            "representations": [
                {
                    "resolution": "1920x1080",
                    "framerate": 30.0,
                    "bitrate": "5100",
                    "input": "tos_L1_1920x1080@30_60.mp4"
                }
            ],
            "segmentDuration": "2",
            "fragmentType": "duration",
            "hasSEI": false,
            "hasVUITiming": true,
            "visualSampleEntry": "FALSE",
            "mpdPath": "https://dash.akamaized.net/WAVE/vectors/2021-06-11/avc_sets/15_30_60/t1/stream.mpd",
            "zipPath": "https://dash.akamaized.net/WAVE/vectors/2021-06-11/avc_sets/15_30_60/t1.zip"
        }
    }
}
```

## Search Syntax

You can browse files directly, or just use the simple search syntax that is available in the search field on the top of the page.

For example, if you want to isolate files that have a 5 second segment duration just type `segmentDuration==5`,
if you want to search files with segmentDuration at 5 and fragmentType at "duration", just type `segmentDuration==5:fragmentType==duration`.

The `:` character acts as a logical **AND**.
