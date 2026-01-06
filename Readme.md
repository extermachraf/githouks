# 🪝 Git Hooks Practice Repository

A comprehensive hands-on guide to understanding and implementing Git hooks with practical examples focused on security and code quality automation.

## 📚 Table of Contents

- [What are Git Hooks?](#what-are-git-hooks)
- [Why Use Git Hooks?](#why-use-git-hooks)
- [Tyks](#types-of-git-hooks)
- [Getting pes of Git HooStarted](#getting-started)
- [Repository Structure](#repository-structure)
- [Implemented Hooks](#implemented-hooks)
- [Usage Examples](#usage-examples)
- [Best Practices](#best-practices)
- [Common Issues](#common-issues)

---

## 🎯 What are Git Hooks?

Git hooks are **scripts that Git executes automatically** before or after certain events such as commit, push, merge, and more. They live in the `.git/hooks` directory of your repository and allow you to:

- Enforce coding standards
- Run automated tests
- Prevent sensitive data leaks
- Validate commit messages
- Automate deployment workflows
- Lint code before commits

Think of them as **automated gatekeepers** that ensure quality and security standards are met before changes enter your codebase.

---

## 💡 Why Use Git Hooks?

### Security Benefits

- 🔐 **Prevent credential leaks**: Stop API keys, passwords, and tokens from being committed
- 🛡️ **Catch secrets early**: Identify sensitive data before it reaches remote repositories
- 🚨 **Enforce security policies**: Automatically scan for security vulnerabilities

### Code Quality Benefits

- ✅ **Maintain standards**: Enforce linting, formatting, and style guidelines
- 🧪 **Run tests automatically**: Ensure tests pass before commits
- 📝 **Validate commit messages**: Keep git history clean and meaningful
- 🎨 **Format code consistently**: Auto-format code to match team standards

### Workflow Benefits

- ⚡ **Catch errors early**: Find issues before code review
- 🚀 **Automate repetitive tasks**: No more manual checks
- 👥 **Team consistency**: Everyone follows the same rules
- 💰 **Save time**: Prevent broken code from entering the pipeline

---

## 🔧 Types of Git Hooks

### Client-Side Hooks

These run on your local machine:

| Hook                   | Trigger                            | Common Use Cases                              |
| ---------------------- | ---------------------------------- | --------------------------------------------- |
| **pre-commit**         | Before commit is created           | Lint code, check formatting, scan for secrets |
| **prepare-commit-msg** | Before commit message editor opens | Auto-generate commit message templates        |
| **commit-msg**         | After commit message is written    | Validate commit message format                |
| **post-commit**        | After commit is created            | Send notifications, update logs               |
| **pre-push**           | Before push to remote              | Run tests, verify build                       |
| **post-merge**         | After successful merge             | Install dependencies, rebuild project         |
| **post-checkout**      | After checkout                     | Clean build artifacts, setup environment      |

### Server-Side Hooks

These run on the Git server:

| Hook             | Trigger                      | Common Use Cases                |
| ---------------- | ---------------------------- | ------------------------------- |
| **pre-receive**  | Before accepting push        | Enforce policies, run CI/CD     |
| **update**       | Once per branch being pushed | Branch-specific rules           |
| **post-receive** | After push is accepted       | Deploy code, send notifications |

---

## 🚀 Getting Started

### Prerequisites

```bash
# Check Git version (2.9+ recommended)
git --version

# For Python hooks in this repo
python3 --version
pip install flake8
```

### Setup

1. **Clone this repository**:

   ```bash
   git clone <repository-url>
   cd githouks-practice
   ```

2. **Configure Git to use custom hooks directory**:

   ```bash
   git config core.hooksPath .githooks
   ```

   This tells Git to look for hooks in `.githooks/` instead of `.git/hooks/`.

3. **Make hooks executable**:

   ```bash
   chmod +x .githooks/*
   ```

4. **Install Python dependencies** (for code quality checks):
   ```bash
   pip install flake8
   ```

### Verify Setup

Try making a commit with secrets or code quality issues:

```bash
# This should be blocked by the pre-commit hook
echo 'api_key = "sk-test-1234567890"' >> test.py
git add test.py
git commit -m "test hook"
```

You should see the hook block the commit with detailed error messages! 🎉

---

## 📁 Repository Structure

```
githouks-practice/
├── .githooks/              # Custom Git hooks directory
│   ├── pre-commit         # Main security & quality hook
│   ├── commit-msg         # Commit message validation
│   ├── post-merge         # Post-merge automation
├── app/
│   └── main.py            # Sample FastAPI application
├── Readme.md              # This file
└── .gitignore
```

---

## 🛠️ Implemented Hooks

### 1. Pre-Commit Hook (Security & Quality)

**Location**: `.githooks/pre-commit`

**Purpose**: Prevents commits containing secrets or code quality issues.

**Features**:

- 🔐 **Secret Detection** - Scans for:
  - API keys (Google, AWS, Stripe, etc.)
  - Access tokens and OAuth tokens
  - Passwords and secrets in variable names
  - Database connection strings
  - Private keys (RSA, EC, DSA)
  - GitHub Personal Access Tokens
- 🐍 **Python Code Quality** - Checks:
  - Syntax errors
  - PEP 8 style violations (via flake8)
  - Unused imports and variables
  - Line length limits
  - Whitespace issues

**How it works**:

1. Scans all staged files
2. Runs regex patterns to detect secrets
3. Validates Python files with flake8
4. Displays formatted errors if issues found
5. **Both checks always run** - even if one fails
6. Blocks commit if any issues detected

**Example Output**:

```
═══════════════════════════════════════════════════════════
   🛡️  PRE-COMMIT VALIDATION STARTED
═══════════════════════════════════════════════════════════
🔐 Scanning for secrets and credentials...

╔═══════════════════════════════════════════════════════╗
║  🚨  SECURITY ALERT - SECRETS DETECTED  🚨           ║
╚═══════════════════════════════════════════════════════╝

📄 File: app/main.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ⚠️  Line 10:    aws_access_key = "AKIAIOSFODNN7EXAMPLE"

❌ Commit blocked: Potential secrets found in staged files.
💡 Tip: Use environment variables or secret management tools.
```

### 2. Commit-Msg Hook

**Location**: `.githooks/commit-msg`

**Purpose**: Validates commit message format.

**Features**:

- Enforces conventional commits format
- Checks minimum message length
- Prevents vague messages like "fix" or "update"

### 3. Post-Merge Hook

**Location**: `.githooks/post-merge`

**Purpose**: Automates post-merge tasks.

**Features**:

- Installs/updates dependencies
- Cleans build artifacts
- Runs database migrations
- Notifies team of merge

## 📖 Usage Examples

### Example 1: Testing Secret Detection

**Try committing a file with secrets**:

```bash
# Create a file with an API key
cat << EOF > config.py
api_key = "AIzaSyAbC123456789_test"
database_url = "postgresql://user:password123@localhost/db"
EOF

# Try to commit
git add config.py
git commit -m "add config"
```

**Result**: ❌ Commit blocked with detailed error showing exactly which lines contain secrets.

**Fix**:

```python
# Use environment variables instead
import os
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
```

### Example 2: Testing Code Quality Checks

**Try committing Python code with issues**:

```bash
cat << EOF > bad_code.py
import sys  # Unused import
import os   # Unused import

def hello():
    x=1+2  # Missing spaces
    very_long_line_that_exceeds_the_recommended_79_character_limit_for_python_code_according_to_pep8 = "test"
    return "hi"
EOF

git add bad_code.py
git commit -m "add code"
```

**Result**: ❌ Commit blocked with flake8 errors listed.

**Fix**: Clean up the code:

```python
def hello():
    x = 1 + 2  # Proper spacing
    result = "test"  # Shorter variable name
    return "hi"
```

### Example 3: Successful Commit

**Clean code with no secrets**:

```bash
cat << EOF > clean_code.py
"""A simple greeting module."""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
EOF

git add clean_code.py
git commit -m "feat: add greeting module"
```

**Result**: ✅ All checks pass, commit successful!

```
═══════════════════════════════════════════════════════════
   ✅  ALL CHECKS PASSED - Proceeding with commit
═══════════════════════════════════════════════════════════
```

### Example 4: Bypassing Hooks (Use Carefully!)

In rare cases where you need to bypass hooks:

```bash
git commit --no-verify -m "emergency fix"
```

⚠️ **Warning**: Only use `--no-verify` in emergencies. It defeats the purpose of hooks!

---

## 🎓 Best Practices

### For Security Hooks

1. ✅ **Always scan for secrets** before committing
2. ✅ **Use environment variables** for sensitive data
3. ✅ **Use secret management tools** (AWS Secrets Manager, HashiCorp Vault)
4. ✅ **Regularly update secret patterns** as new services emerge
5. ❌ **Never use** `--no-verify` to bypass security checks

### For Code Quality Hooks

1. ✅ **Run hooks locally** before pushing
2. ✅ **Keep hooks fast** (< 5 seconds when possible)
3. ✅ **Provide clear error messages** with solutions
4. ✅ **Make hooks project-specific** to match your needs
5. ✅ **Document hook requirements** in README

### General Hook Guidelines

1. ✅ **Make hooks executable** (`chmod +x`)
2. ✅ **Test hooks thoroughly** before deploying
3. ✅ **Use exit codes properly** (0 = success, 1 = failure)
4. ✅ **Handle errors gracefully** with helpful messages
5. ✅ **Version control your hooks** (use `.githooks/` directory)

---

## 🔍 Customizing Hooks

### Adding New Secret Patterns

Edit `.githooks/pre-commit` and add to the `patterns` array:

```bash
local patterns=(
    # Your custom pattern
    "my_custom_secret[[:space:]]*[=:][[:space:]]*['\"][a-zA-Z0-9]{20,}"
    # ... existing patterns
)
```

### Adjusting Flake8 Rules

Create a `.flake8` configuration file:

```ini
[flake8]
max-line-length = 100
ignore = E203, W503
exclude = .git,__pycache__,venv
```

### Disabling Specific Checks

Temporarily disable a check by commenting it out:

```bash
# validate_code_quality
# if [ $? -ne 0 ]; then
#     quality_failed=1
# fi
```

---

## ⚠️ Common Issues

### Issue 1: Hooks Not Running

**Problem**: Commits succeed without running hooks.

**Solutions**:

```bash
# Check hooks path
git config core.hooksPath

# Set it if not configured
git config core.hooksPath .githooks

# Verify hooks are executable
ls -l .githooks/
chmod +x .githooks/*
```

### Issue 2: "Permission Denied" Error

**Problem**: Hook script lacks execute permission.

**Solution**:

```bash
chmod +x .githooks/pre-commit
```

### Issue 3: Python Module Not Found

**Problem**: `ModuleNotFoundError: No module named 'flake8'`

**Solution**:

```bash
# Install flake8
pip install flake8

# Or use conda
conda install flake8
```

### Issue 4: Hooks Too Slow

**Problem**: Hooks take too long to run.

**Solutions**:

- Only check staged files (not entire project)
- Cache linting results
- Run heavy checks in pre-push instead of pre-commit
- Parallelize independent checks

### Issue 5: False Positives in Secret Detection

**Problem**: Hook flags non-secrets as secrets.

**Solutions**:

- Refine regex patterns to be more specific
- Add file/line exclusions
- Use comments to mark false positives: `# noqa: secret`

---
