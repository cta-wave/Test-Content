# Test-Content

This page collects information around CTA WAVE Test Content.

CTA WAVE Test Content is hosted here: https://dash.akamaized.net/WAVE/index.html


How to add content:
* Original Content: Submit an [issue](https://github.com/cta-wave/Test-Content/issues/new&labels=proposed-original)
* Proposed CTA WAVE Content: Submit an [issue](https://github.com/cta-wave/Test-Content/issues/new&labels=proposed-wave-content) 

## How does this site work

This website is a SPA coded using Vue.js and PureCSS, it relies on a flat file json database you can find [here](http://dash.akamaized.net/WAVE/js/app.js)

The database is an object containing attributes discribing each asset.

Each asset has its own idea, generated from the content matrix, and its main type, and the object contains the representations, and how the content was generated.

```
{
    "wave_avc_sets_1": {
        "representations": [
            {
                "resolution": "1920x1080",
                "framerate": 60,
                "bitrate": 7800,
                "input": "content_files/tos_O1_3840x2160@60_60.mp4"
            },
            {
                "resolution": "1920x1080",
                "framerate": 60,
                "bitrate": 6000,
                "input": "content_files/tos_O2_3840x2160@60_60.mp4"
            },
            {
                "resolution": "1280x720",
                "framerate": 60,
                "bitrate": 4500,
                "input": "content_files/tos_O3_3840x2160@60_60.mp4"
            },
            {
                "resolution": "1280x720",
                "framerate": 60,
                "bitrate": 3000,
                "input": "content_files/tos_N1_3200x1800@60_60.mp4"
            },
            {
                "resolution": "768x432",
                "framerate": 30,
                "bitrate": 1100,
                "input": "content_files/tos_M1_2560x1440@60_60.mp4"
            },
            {
                "resolution": "768x432",
                "framerate": 30,
                "bitrate": 730,
                "input": "content_files/tos_L1_1920x1080@60_60.mp4"
            }
        ],
        "segmentDuration": "2",
        "fragmentType": "duration",
        "hasSEI": true,
        "hasVUITiming": true,
        "visualSampleEntry": "avc1",
        "mpdPath": "avc_sets/1/stream.mpd"
    }
}
```

## Search Syntax

You can browse files directly, or just use the simple search syntax that is available in the search field on the top of the page.

For example, if you want to isolate files that have a 5 second segment duration just type `segmentDuration==5`,
if you want to search files with segmentDuration at 5 and fragmentType at "duration", just type `segmentDuration==5:fragmentType==duration`.

The `:` character acts as a logical **AND**.
