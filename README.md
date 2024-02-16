# Django Zoo API

This Django-based API allows you to manage categories and animals for a zoo. It provides endpoints for creating, updating, deleting, and retrieving categories and animals. Additionally, it supports caching for animal lists and batch deletion of animals.

## Installation

1. Clone the repository:
git clone github.com/konstantine25b/Zoo_API
cd Zoo_API
2. Install the required dependencies:
pip install -r requirements.txt
3. Apply migrations:
python manage.py migrate


## Usage

### Categories

#### List Categories
GET /categories/
#### Retrieve Category
GET /animals/
#### Retrieve Animal

Filtering
You can filter animals by name, category, and status:
GET /animals/?name=<animal-name>&category=<category-id>&status=<animal-status>
