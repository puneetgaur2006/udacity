def format_game_response(document, source="Local Dataset", confidence="High"):
    
    try:
        # Try to parse structured game object
        game = eval(document)

        response = f"""
🎮 Game Information Report

Title: {game.get('title')}
Developer: {game.get('developer')}
Publisher: {game.get('publisher')}
Release Date: {game.get('release_date')}
Platforms: {', '.join(game.get('platforms', []))}
Genre: {game.get('genre')}

Source: {source}
Confidence: {confidence}
"""
        return response

    except:
        # If document is plain text (web knowledge)
        response = f"""
📚 Information

{document}

Source: {source}
Confidence: {confidence}
"""
        return response