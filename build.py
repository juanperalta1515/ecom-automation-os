"""
Netlify / Static Deployment Builder for E-Com Automation OS
Bundles app.py and all modules into a standalone client-side WebAssembly Streamlit application (stlite) for 1-click Netlify deployment.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_file_content(relative_path: str) -> str:
    full_path = os.path.join(BASE_DIR, relative_path)
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_static_bundle():
    files_map = {
        "app.py": read_file_content("app.py"),
        "modules/__init__.py": read_file_content("modules/__init__.py"),
        "modules/product_catalog.py": read_file_content("modules/product_catalog.py"),
        "modules/product_radar.py": read_file_content("modules/product_radar.py"),
        "modules/validation_blueprint.py": read_file_content("modules/validation_blueprint.py"),
        "modules/ai_creative_factory.py": read_file_content("modules/ai_creative_factory.py"),
        "modules/ads_analytics.py": read_file_content("modules/ads_analytics.py"),
        "modules/sourcing_hub.py": read_file_content("modules/sourcing_hub.py"),
        "modules/knowledge_base.py": read_file_content("modules/knowledge_base.py"),
        "data/rules.json": read_file_content("data/rules.json"),
    }

    files_json = json.dumps(files_map)

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <title>E-Com Automation OS | Scale & Validation Engine</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.73.1/build/stlite.css" />
  <style>
    body, html {{
      margin: 0;
      padding: 0;
      height: 100%;
      background-color: #0e1117;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    #root {{
      height: 100vh;
    }}
  </style>
</head>
<body>
  <div id="root"></div>
  <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.73.1/build/stlite.js"></script>
  <script>
    const files = {files_json};
    
    stlite.mount({{
      requirements: ["pandas", "requests"],
      entrypoint: "app.py",
      files: files
    }}, document.getElementById("root"));
  </script>
</body>
</html>
"""

    dist_dir = os.path.join(BASE_DIR, "dist")
    os.makedirs(dist_dir, exist_ok=True)

    # Write index.html to dist/
    dist_html_path = os.path.join(dist_dir, "index.html")
    with open(dist_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    # Also write index.html to root for direct static hosting
    root_html_path = os.path.join(BASE_DIR, "index.html")
    with open(root_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Build completed successfully! Generated: {dist_html_path} and {root_html_path}")

if __name__ == "__main__":
    generate_static_bundle()
