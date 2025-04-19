import random

# Diccionarios con términos cool y cyberpunk
adjectives = [
    "neon", "cyber", "dark", "quantum", "holographic", "synthetic", "digital", "electric",
    "virtual", "futuristic", "mechanical", "infinite", "parallel", "hyper", "glitch", "shadow",
    "chrome", "liquid", "stellar", "lunar", "solar", "plasma", "vortex", "nano", "meta",
    "prismatic", "phantom", "radial", "binary", "static", "kinetic", "magnetic", "cosmic",
    "orbital", "spectral", "adaptive", "dynamic", "encrypted", "hacked", "augmented", "wired",
    # Agrega más términos hasta llegar a 400
] * 10  # Multiplicamos para simular 400 términos

nouns = [
    "spectrum", "matrix", "memory", "system", "network", "protocol", "signal", "core",
    "circuit", "interface", "module", "algorithm", "processor", "cluster", "grid", "node",
    "array", "framework", "datastream", "firewall", "gateway", "hub", "link", "packet",
    "sensor", "terminal", "unit", "vector", "wave", "zone", "engine", "drive", "field",
    "pulse", "quantum", "shell", "thread", "vault", "web", "zone", "cyberspace",
    # Agrega más términos hasta llegar a 400
] * 10  # Multiplicamos para simular 400 términos

modifiers = [
    "native", "synthetic", "virtual", "holographic", "encrypted", "adaptive", "dynamic",
    "parallel", "infinite", "prismatic", "augmented", "kinetic", "magnetic", "cosmic",
    "orbital", "stellar", "lunar", "solar", "plasma", "vortex", "nano", "meta", "phantom",
    "radial", "binary", "static", "liquid", "shadow", "chrome", "glitch", "wired", "quantum",
    "cybernetic", "mechanical", "digital", "electric", "futuristic", "dark", "neon", "hyper",
    # Agrega más términos hasta llegar a 400
] * 10  # Multiplicamos para simular 400 términos

def generate_song_titles():
    """Genera 40 nombres aleatorios combinando términos de los diccionarios."""
    titles = set()
    while len(titles) < 40:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        modifier = random.choice(modifiers)
        title = f"{adjective}_{noun}_{modifier}"
        titles.add(title)
    return list(titles)

# Ejemplo de uso
if __name__ == "__main__":
    song_titles = generate_song_titles()
    for title in song_titles:
        print(title)
