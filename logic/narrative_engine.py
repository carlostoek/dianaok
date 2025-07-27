import json

def get_story_fragment(fragment_id):
    with open('data/story_fragments.json', 'r') as f:
        story_fragments = json.load(f)
    return story_fragments.get(str(fragment_id), {"content": "Fragmento no encontrado", "options": []})