from flask import Blueprint, request, jsonify
from models import Profile, Project
from app import db
from flask_jwt_extended import jwt_required

project_bp = Blueprint('project', __name__)

# Get Profile List (paginated)
@project_bp.route('/profiles', methods=['GET'])
@jwt_required()
def get_profiles():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    profiles = Profile.query.paginate(page=page, per_page=per_page)
    return jsonify([{'id': p.id, 'name': p.name} for p in profiles.items])

# Get Projects for a specific profile
@project_bp.route('/projects/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_projects(profile_id):
    projects = Project.query.filter_by(profile_id=profile_id).all()
    if projects:
        return jsonify([{'name': p.name, 'description': p.description} for p in projects])
    return jsonify({'message': 'No projects found'}), 404
