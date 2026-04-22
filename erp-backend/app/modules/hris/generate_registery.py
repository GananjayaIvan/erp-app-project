import os
import ast

MODELS_PATH = os.path.join(
    os.path.dirname(__file__),
    "models"
)

OUTPUT_FILE = os.path.join(
    os.path.dirname(__file__),
    "registry.py"
)


def is_sqlalchemy_model(class_node):
    """
    Detect if class inherits from Base
    """
    for base in class_node.bases:
        if isinstance(base, ast.Name) and base.id == "Base":
            return True
        if isinstance(base, ast.Attribute) and base.attr == "Base":
            return True
    return False


def extract_model_classes(file_path):
    """
    Extract only SQLAlchemy models
    """
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    models = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            if is_sqlalchemy_model(node):
                models.append(node.name)

    return models


def generate_registry():
    model_files = sorted([
        f for f in os.listdir(MODELS_PATH)
        if f.endswith(".py") and f != "__init__.py"
    ])

    imports = []
    all_models = []

    for file in model_files:
        module_name = file.replace(".py", "")
        file_path = os.path.join(MODELS_PATH, file)

        try:
            classes = extract_model_classes(file_path)

            if classes:
                imports.append(
                    f"from app.modules.hris.models.{module_name} import {', '.join(classes)}"
                )
                all_models.extend(classes)

        except Exception as e:
            print(f"Skipping {file}: {e}")

    registry_content = "\n".join(imports)
    registry_content += "\n\nHRIS_MODELS = [\n"

    for model in sorted(all_models):
        registry_content += f"    {model},\n"

    registry_content += "]\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(registry_content)

    print(f"Registry generated with {len(all_models)} models.")


if __name__ == "__main__":
    generate_registry()