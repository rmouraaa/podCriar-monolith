import httpx
import os
from typing import Optional, Dict

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
MODEL_NAME = "gemma:2b"
TIMEOUT = 60.0


async def generate_podcast_script(
    theme: str,
    duration: str,
    tone: str
) -> Dict[str, any]:
    prompt = f"""You are an expert podcast scriptwriter.
Your task is to write a complete podcast script ready to be spoken aloud.
Follow these creative and formatting rules carefully:

STRUCTURE:
- Include a captivating introduction that immediately hooks the listener.  
- Develop the main content with relevant insights, curiosities, and engaging storytelling.  
- Finish with a memorable conclusion that closes the episode naturally.  
- Use natural, fluid, and conversational language — as if the host were speaking directly to the audience.  
- The total script should be approximately {duration} long when spoken.

PARAGRAPHING RULES:
- Always write in short paragraphs to make it easier to generate and adjust one paragraph at a time.  
- If the tone, subject, or emotion of a section remains consistent, you may merge ideas into a slightly longer paragraph to preserve natural voice flow.  
- Each paragraph should represent a coherent speech segment.

FORMATTING DIRECTIVES:
- Names of people or speakers must appear **between double asterisks**, e.g., **Rodrigo**, to indicate voice lines.  
- If a segment requires or benefits from background music, specify it inside curly braces, e.g., {{soft ambient background music}}.  
- When a sound effect is needed, specify it inside square brackets, e.g., [door opening sound].  
- If a section requires an intro, transition, or outro theme, place it inside parentheses, e.g., (Podcast intro jingle starts).  
- If there is any public domain audio content that could enrich the episode (like an interview, speech, or archive clip), mention it between double dashes, e.g., --Excerpt from Kennedy's speech (public domain, source: X)--.

Theme: {theme}
Duration: {duration}
Tone: {tone}

GOAL:
Generate a complete, ready-to-record script that follows the structure and notation above, producing it naturally paragraph by paragraph.

Begin the script now:"""

    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()

            data = response.json()
            script = data.get("response", "")

            if not script:
                return {
                    "success": False,
                    "error": "Ollama returned empty response"
                }

            return {
                "success": True,
                "script": script,
                "model": MODEL_NAME
            }

    except httpx.TimeoutException:
        return {
            "success": False,
            "error": f"Ollama timeout after {TIMEOUT} seconds"
        }
    except httpx.RequestError as e:
        return {
            "success": False,
            "error": f"Failed to connect to Ollama: {str(e)}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }
