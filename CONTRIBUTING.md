# Contributing to AI Chatbot

We welcome contributions! Here's how you can help.

## Getting Started

1. **Fork the repository** - Click the fork button on GitHub
2. **Clone your fork** - `git clone https://github.com/YOUR_USERNAME/ai-chatbot.git`
3. **Create a branch** - `git checkout -b feature/amazing-feature`
4. **Make changes** - Edit files as needed
5. **Commit** - `git commit -m 'Add amazing feature'`
6. **Push** - `git push origin feature/amazing-feature`
7. **Open a Pull Request** - Submit your changes for review

## Development Setup

### Python Backend
```bash
cd backend-python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API key
python app.py
```

### Node.js Backend
```bash
cd backend-node
npm install
cp .env.example .env
# Edit .env with your API key
npm run dev
```

### Frontend Development
```bash
cd frontend
python -m http.server 8000
# Open http://localhost:8000
```

## Testing

### Test Python Backend
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello","user_id":"test"}'
```

### Test Node Backend
```bash
curl -X POST http://localhost:5001/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello","user_id":"test"}'
```

## Code Style

### Python
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions

### JavaScript
- Use 2-space indentation
- Use const/let instead of var
- Add comments for complex logic

## Commit Message Guidelines

Use clear, descriptive commit messages:
- ✅ `Add voice input feature to frontend`
- ✅ `Fix rate limiting bug in Python backend`
- ✅ `Update README with setup instructions`
- ❌ `fix bug`
- ❌ `update files`

## Pull Request Guidelines

1. **Clear Title** - Describe what the PR does
2. **Description** - Explain the changes and why
3. **Testing** - Confirm you've tested the changes
4. **Screenshots** - Add UI changes screenshots
5. **Issues** - Link related issues with "Closes #123"

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tested locally
- [ ] Added tests
- [ ] All tests pass

## Checklist
- [ ] Code follows style guidelines
- [ ] Comments added where needed
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Reporting Issues

### Bug Reports
Include:
- Clear title
- Detailed description
- Steps to reproduce
- Expected vs actual behavior
- Error messages/screenshots
- System info (OS, browser, etc.)

### Feature Requests
Include:
- Clear title
- Why this feature would be useful
- How it should work
- Any alternative solutions

## Areas for Contribution

- **Features**: Voice profiles, language support, custom personalities
- **Improvements**: Performance, UI/UX, error handling
- **Documentation**: READMEs, guides, examples
- **Testing**: Unit tests, integration tests
- **Deployment**: Docker, CI/CD pipelines
- **Bug Fixes**: Reported issues

## Questions?

- Check existing issues and discussions
- Ask in GitHub Discussions
- Check the README and docs first

## License

By contributing, you agree your code will be under the MIT License.

Thanks for contributing! 🎉
