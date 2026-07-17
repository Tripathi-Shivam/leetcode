## Playlist Duration Calculation: YouTube

**Context**
The objective is to calculate the total duration of all videos in a YouTube playlist. The user's original script failed because it relied on the deprecated `span.ytd-thumbnail-overlay-time-status-renderer` selector, which is no longer present in the current YouTube UI.

**Diagnostics**
An inspection of the playlist page (specifically `https://www.youtube.com/playlist?list=...`) revealed the following:

| Metric/Selector | Result |
| :--- | :--- |
| Target Page Type | Playlist View |
| Original Selector | 0 elements found |
| New Timestamp Element | `badge-shape` |
| Timestamp Parent | `yt-thumbnail-badge-view-model` |
| Observed Data Formats | `MM:SS`, `H:MM:SS` |

**Actionable Findings**
* **Selector Update:** YouTube now uses a custom element `badge-shape` with specific classes to display video durations on thumbnails.
* **Parsing Logic:** The script must account for the `innerText` of these badge elements and correctly handle both two-part (MM:SS) and three-part (HH:MM:SS) time strings.
* **Limitations:** This calculation only totals the durations currently rendered in the DOM. For long playlists, the user must scroll to the bottom to ensure all videos are loaded before running the script.

**Code Fixes**
The following updated script targets the correct `badge-shape` elements and calculates the total duration based on the live page structure:


`````js
let totalSeconds = 0;

// Target the badge-shape elements that contain the timestamps
const timeBadges = document.querySelectorAll('badge-shape.ytBadgeShapeThumbnailBadge');

timeBadges.forEach(badge => {
  const text = badge.innerText.trim();
  // Regex ensures we only process strings that look like timestamps
  if (/^\d{1,2}(:\d{2}){1,2}$/.test(text)) {
    const parts = text.split(':').map(Number);
    
    if (parts.length === 3) { // HH:MM:SS
      totalSeconds += parts[0] * 3600 + parts[1] * 60 + parts[2];
    } else if (parts.length === 2) { // MM:SS
      totalSeconds += parts[0] * 60 + parts[1];
    }
  }
});

const h = Math.floor(totalSeconds / 3600);
const m = Math.floor((totalSeconds % 3600) / 60);
const s = totalSeconds % 60;

console.log(`Total Playlist Duration: ${h}h ${m}m ${s}s`);

`````

*Note: The code fixes and findings above were identified on a live page in DevTools. When applying them to your codebase, please adapt them to your project's specific technical stack (e.g., Tailwind CSS classes, CSS modules, framework components) rather than applying them as literal CSS overrides.*