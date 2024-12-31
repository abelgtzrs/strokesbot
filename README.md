# The Strokes Lyrics Twitter Bot 🎸

A Twitter bot that tweets iconic lyrics from **The Strokes** every 30 minutes, followed by a reply with the song name and album information.

---

## Features 🚀

- Tweets a random lyric from a list of **The Strokes** songs.
- Replies to each tweet with the corresponding song title and album.
- Uses Python and Tweepy for easy integration with the Twitter API.

---

## How It Works 🛠️

1. **Lyrics Storage**:
   - Lyrics, song titles, and album names are stored in a structured Python dictionary (`lyrics_data`).

2. **Random Selection**:
   - The bot selects a random lyric from the `lyrics_data` object for each tweet.

3. **Tweet and Reply**:
   - Posts a lyric as a tweet.
   - Automatically replies with the song name and album.

4. **Timing**:
   - Waits 30 minutes between tweets to maintain consistency and comply with Twitter's rate limits.

---

## Requirements 📋

- Python 3.7 or higher
- Twitter Developer Account with API keys
- Tweepy Library
