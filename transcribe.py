from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTranscriber:
    def __init__(self, youtube_link):
        self.youtube_link = youtube_link

    def get_transcription(self):
        try:
            video_id = self._extract_video_id()
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            text = self._format_transcript(transcript)
            return text
        except Exception as e:
            return f"Error: {str(e)}"

    def _extract_video_id(self):
        # Extract video ID from the YouTube link
        if "youtube.com" in self.youtube_link:
            video_id = self.youtube_link.split("v=")[1]
            ampersand_pos = video_id.find("&")
            if ampersand_pos != -1:
                video_id = video_id[:ampersand_pos]
        elif "youtu.be" in self.youtube_link:
            video_id = self.youtube_link.split("/")[-1]
        else:
            raise ValueError("Invalid YouTube link format")
        return video_id

    def _format_transcript(self, transcript):
        # Format the transcript into plain text without audio timestamps and content within square brackets
        text = ""
        for entry in transcript:
            # Ignore content within square brackets
            entry_text = entry['text']
            entry_text = ' '.join(
                word for word in entry_text.split() if not (word.startswith('[') and word.endswith(']')))

            text += f"{entry_text}\n"
        return text
