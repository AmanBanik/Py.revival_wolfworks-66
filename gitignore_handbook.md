# The Complete .gitignore Handbook

## Table of Contents
1. [Introduction](#introduction)
2. [Why .gitignore Matters](#why-gitignore-matters)
3. [Basic Syntax](#basic-syntax)
4. [Protection Scenarios](#protection-scenarios)
5. [Language-Specific Patterns](#language-specific-patterns)
6. [Framework-Specific Patterns](#framework-specific-patterns)
7. [Common Patterns Library](#common-patterns-library)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## Introduction

The `.gitignore` file is a critical configuration file that tells Git which files and directories to ignore in a project. It prevents sensitive, unnecessary, or auto-generated files from being tracked in version control.

---

## Why .gitignore Matters

### Security Protection
- **API Keys & Secrets**: Prevents accidental exposure of credentials
- **Environment Variables**: Protects `.env` files containing sensitive configuration
- **Certificates & Keys**: Keeps SSL certificates and private keys out of version control
- **Database Credentials**: Protects database connection strings and passwords

### Repository Cleanliness
- **Build Artifacts**: Excludes compiled code that can be regenerated
- **Dependencies**: Prevents tracking of node_modules, vendor folders, etc.
- **Logs**: Keeps log files out of the repository
- **Temporary Files**: Excludes cache and temporary system files

### Performance Benefits
- **Faster Operations**: Smaller repositories mean faster clone, push, and pull operations
- **Reduced Storage**: Saves space on local machines and remote servers
- **Efficient Diffs**: Cleaner commit history without noise from generated files

### Team Collaboration
- **IDE Consistency**: Ignores IDE-specific files that differ between team members
- **OS Differences**: Handles OS-specific files (macOS, Windows, Linux)
- **Personal Settings**: Allows developers to have personal configuration without conflicts

---

## Basic Syntax

### Comment Lines
```
# This is a comment
```

### Ignore Specific File
```
secret.txt
config.local.js
```

### Ignore All Files with Extension
```
*.log
*.tmp
*.pyc
```

### Ignore Directory
```
node_modules/
build/
dist/
```

### Negation (Don't Ignore)
```
# Ignore all .log files
*.log

# But don't ignore important.log
!important.log
```

### Wildcard Patterns
```
# Match any character except /
*.txt

# Match zero or more directories
**/logs

# Match files in any subdirectory
**/build/*.js
```

### Range Patterns
```
# Ignore file0.txt through file9.txt
file[0-9].txt

# Ignore fileA.txt through fileZ.txt
file[A-Z].txt
```

### Double Asterisk (Recursive)
```
# Ignore logs directory anywhere in the tree
**/logs/

# Ignore all .pdf files in any docs folder
**/docs/**/*.pdf
```

---

## Protection Scenarios

### 1. Protecting Sensitive Credentials

**Scenario**: Developer accidentally commits API keys to public repository

**Protection**:
```
# Environment variables
.env
.env.local
.env.*.local
.env.development
.env.production
.env.test

# API Keys and secrets
secrets.yml
secrets.json
*-secret.json
*.key
*.pem

# AWS credentials
.aws/
credentials

# Google Cloud credentials
*-credentials.json
service-account.json

# Azure credentials
*.publishsettings
```

### 2. Protecting Database Information

**Scenario**: Database dumps or connection strings exposed

**Protection**:
```
# Database files
*.sql
*.sqlite
*.db
*.mdb

# Database dumps
dump/
*.dump
backup.sql

# Database configuration
database.yml
database.json
db-config.js
```

### 3. Protecting Personal Information

**Scenario**: User data or PII accidentally committed

**Protection**:
```
# User uploads
uploads/
user-files/
attachments/

# CSV/Excel with sensitive data
sensitive-*.csv
personal-data.xlsx
user-list.*

# Reports with personal info
reports/sensitive/
```

### 4. Preventing Dependency Bloat

**Scenario**: Massive node_modules folder slowing down operations

**Protection**:
```
# JavaScript/Node
node_modules/
npm-debug.log
yarn-error.log
package-lock.json  # If using yarn
yarn.lock          # If using npm

# Python
venv/
env/
.venv/
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/

# Ruby
vendor/bundle/
.bundle/

# PHP
vendor/
composer.lock  # Optional, team decision

# Go
vendor/
go.sum  # Optional

# .NET
packages/
bin/
obj/
```

### 5. Protecting Build Artifacts

**Scenario**: Compiled code causing merge conflicts

**Protection**:
```
# JavaScript builds
dist/
build/
out/
.next/
.nuxt/
.output/

# Java
target/
*.class
*.jar
*.war

# C/C++
*.o
*.so
*.exe
*.out
a.out

# Python
*.pyc
__pycache__/
*.so
.Python
```

### 6. Protecting IDE and OS Files

**Scenario**: Team members use different IDEs causing conflicts

**Protection**:
```
# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store
Thumbs.db

# JetBrains
.idea/
*.iml
*.iws

# Visual Studio
.vs/
*.suo
*.user

# Eclipse
.project
.classpath
.settings/

# Sublime Text
*.sublime-project
*.sublime-workspace
```

### 7. Protecting Cache and Temporary Files

**Scenario**: Cache files causing inconsistencies

**Protection**:
```
# General cache
.cache/
*.cache
cache/
tmp/
temp/

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# OS temporary files
.DS_Store
Thumbs.db
desktop.ini
```

### 8. Protecting Test Coverage and Reports

**Scenario**: Test reports causing unnecessary diffs

**Protection**:
```
# Test coverage
coverage/
.coverage
htmlcov/
.nyc_output/
*.lcov

# Test results
test-results/
junit.xml
*.test
.pytest_cache/
```

---

## Language-Specific Patterns

### JavaScript/Node.js
```
# Dependencies
node_modules/
jspm_packages/

# Production build
dist/
build/
.next/
out/

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Environment
.env
.env.local
.env.*.local

# Cache
.cache/
.eslintcache
.stylelintcache

# TypeScript
*.tsbuildinfo
```

### Python
```
# Byte-compiled
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
env/
ENV/
.venv/

# Distribution
dist/
build/
*.egg-info/
*.egg

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Jupyter
.ipynb_checkpoints/
*.ipynb

# MyPy
.mypy_cache/
```

### Java
```
# Compiled class files
*.class

# Package files
*.jar
*.war
*.ear
*.zip
*.tar.gz
*.rar

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup

# Gradle
.gradle/
build/
gradle-app.setting
!gradle-wrapper.jar

# IDE
.idea/
*.iml
.classpath
.project
.settings/
```

### Ruby
```
# Bundler
.bundle/
vendor/bundle/

# RVM
.rvmrc

# rbenv
.ruby-version
.ruby-gemset

# Rails
/log/*
/tmp/*
!/log/.keep
!/tmp/.keep
/public/system/
/public/uploads/

# Compiled gems
*.gem

# Database
/db/*.sqlite3
/db/*.sqlite3-journal
```

### PHP
```
# Composer
vendor/
composer.phar
composer.lock  # Team decision

# Laravel
.env
/storage/*.key
/public/hot
/public/storage
/storage/*.log

# WordPress
wp-config.php
/wp-content/uploads/
/wp-content/cache/

# Cache
*.cache
cache/
```

### Go
```
# Binaries
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary
*.test

# Output
*.out

# Vendor
vendor/

# Go workspace
go.work

# IDE
.idea/
*.swp
```

### Rust
```
# Build output
target/
Cargo.lock  # For libraries, keep for binaries

# Debug files
**/*.rs.bk

# IDE
.idea/
.vscode/
```

### C/C++
```
# Prerequisites
*.d

# Compiled Object files
*.slo
*.lo
*.o
*.obj

# Precompiled Headers
*.gch
*.pch

# Compiled Dynamic libraries
*.so
*.dylib
*.dll

# Compiled Static libraries
*.lai
*.la
*.a
*.lib

# Executables
*.exe
*.out
*.app

# Build directories
build/
cmake-build-*/
```

---

## Framework-Specific Patterns

### React
```
# Production
/build
/dist

# Development
.cache/

# Testing
/coverage

# Misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
npm-debug.log*
yarn-debug.log*
```

### Next.js
```
# Next.js build output
.next/
out/

# Production
/build

# Misc
.DS_Store
*.pem

# Debug
npm-debug.log*
yarn-debug.log*
.pnpm-debug.log*

# Local env files
.env*.local

# Vercel
.vercel
```

### Vue.js
```
.DS_Store
node_modules/
/dist

# Local env files
.env.local
.env.*.local

# Log files
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Editor directories and files
.idea
.vscode
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
```

### Django
```
*.log
*.pot
*.pyc
__pycache__/
db.sqlite3
db.sqlite3-journal
media/
staticfiles/
.env
venv/
.Python
```

### Rails
```
*.rbc
capybara-*.html
.rspec
/log
/tmp
/db/*.sqlite3
/public/system
/coverage/
/spec/tmp
**.orig
rerun.txt
pickle-email-*.html
.bundle
vendor/bundle
```

### Laravel
```
/node_modules
/public/hot
/public/storage
/storage/*.key
/vendor
.env
.env.backup
.phpunit.result.cache
Homestead.json
Homestead.yaml
npm-debug.log
yarn-error.log
```

### Spring Boot
```
HELP.md
target/
!.mvn/wrapper/maven-wrapper.jar
!**/src/main/**/target/
!**/src/test/**/target/

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr

### NetBeans ###
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/
build/
```

### Flutter
```
# Miscellaneous
*.class
*.log
*.pyc
*.swp
.DS_Store
.atom/
.buildlog/
.history
.svn/

# IntelliJ related
*.iml
*.ipr
*.iws
.idea/

# Flutter/Dart/Pub related
**/doc/api/
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
.packages
.pub-cache/
.pub/
/build/

# Android related
**/android/**/gradle-wrapper.jar
**/android/.gradle
**/android/captures/
**/android/gradlew
**/android/gradlew.bat
**/android/local.properties
**/android/**/GeneratedPluginRegistrant.java

# iOS/XCode related
**/ios/**/*.mode1v3
**/ios/**/*.mode2v3
**/ios/**/*.moved-aside
**/ios/**/*.pbxuser
**/ios/**/*.perspectivev3
**/ios/**/*sync/
**/ios/**/.sconsign.dblite
**/ios/**/.tags*
**/ios/**/.vagrant/
**/ios/**/DerivedData/
**/ios/**/Icon?
**/ios/**/Pods/
**/ios/**/.symlinks/
**/ios/**/profile
**/ios/**/xcuserdata
**/ios/.generated/
**/ios/Flutter/App.framework
**/ios/Flutter/Flutter.framework
**/ios/Flutter/Flutter.podspec
**/ios/Flutter/Generated.xcconfig
**/ios/Flutter/app.flx
**/ios/Flutter/app.zip
**/ios/Flutter/flutter_assets/
**/ios/Flutter/flutter_export_environment.sh
**/ios/ServiceDefinitions.json
**/ios/Runner/GeneratedPluginRegistrant.*
```

---

## Common Patterns Library

### Complete Template for Most Projects
```
# Operating System Files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
Desktop.ini

# IDE Files
.vscode/
.idea/
*.swp
*.swo
*~
.project
.classpath
.settings/
*.sublime-project
*.sublime-workspace

# Environment Variables
.env
.env.local
.env.*.local
.envrc

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Dependencies
node_modules/
vendor/
venv/
env/

# Build Output
dist/
build/
out/
target/
*.exe
*.dll
*.so
*.dylib

# Cache
.cache/
*.cache
tmp/
temp/

# Testing
coverage/
.coverage
.nyc_output/
.pytest_cache/

# Secrets & Keys
*.key
*.pem
*.p12
*.pfx
secrets.yml
credentials.json
```

---

## Best Practices

### 1. Start with a Template
Use GitHub's `.gitignore` templates as a starting point for your language/framework.

### 2. Use Global .gitignore for Personal Files
Create `~/.gitignore_global` for IDE and OS files:
```bash
git config --global core.excludesfile ~/.gitignore_global
```

### 3. Commit .gitignore Early
Add `.gitignore` in your first commit to prevent accidental tracking.

### 4. Don't Ignore Lock Files
Keep `package-lock.json`, `yarn.lock`, `Gemfile.lock`, etc. for reproducible builds.

### 5. Document Exceptions
If you must commit unusual files, document why in comments:
```
# Usually ignore .env files, but .env.example is a template
.env
!.env.example
```

### 6. Review Before Committing
Always check what you're committing:
```bash
git status
git diff --cached
```

### 7. Use Specific Patterns
Be specific rather than overly broad:
```
# Bad - might ignore important files
*config*

# Good - specific to environment configs
.env*
config.local.js
```

### 8. Order Matters
Put specific exceptions after general rules:
```
*.log        # Ignore all logs
!error.log   # But keep error.log
```

### 9. Test Your .gitignore
Use `git check-ignore` to test patterns:
```bash
git check-ignore -v path/to/file
```

### 10. Clean Already-Tracked Files
If you added `.gitignore` late:
```bash
# Remove from Git but keep locally
git rm --cached filename

# Remove entire directory
git rm -r --cached directory/
```

---

## Troubleshooting

### Problem: File Still Being Tracked
**Solution**: Remove from Git cache
```bash
git rm --cached filename
git commit -m "Remove file from tracking"
```

### Problem: .gitignore Not Working
**Causes**:
1. File was already tracked before adding to `.gitignore`
2. Rule written incorrectly
3. Negation pattern overriding ignore

**Solution**:
```bash
# Clear cache and reapply
git rm -r --cached .
git add .
git commit -m "Fix .gitignore"
```

### Problem: Need to Ignore File Everywhere Except One Location
**Solution**:
```
# Ignore everywhere
logs/*.log

# But not in keep-these/
!keep-these/logs/*.log
```

### Problem: Pattern Not Matching
**Debug with**:
```bash
git check-ignore -v path/to/file
```

### Problem: Need to Track Empty Directory
**Solution**: Add `.gitkeep` file
```bash
touch empty-dir/.gitkeep
```
Then in `.gitignore`:
```
empty-dir/*
!empty-dir/.gitkeep
```

### Problem: Accidentally Committed Secrets
**Solution**:
1. Change all exposed secrets immediately
2. Remove from history:
```bash
# Using git-filter-repo (recommended)
git filter-repo --path secrets.env --invert-paths

# Or BFG Repo-Cleaner
bfg --delete-files secrets.env
```
3. Force push to remote
4. Add to `.gitignore`

### Problem: Different Team Members Need Different Ignores
**Solution**: Use `.git/info/exclude` for personal ignores that shouldn't be shared.

---

## Additional Resources

### Useful Commands
```bash
# Show what would be cleaned
git clean -n

# Remove untracked files
git clean -f

# Remove untracked directories
git clean -fd

# Remove ignored files too
git clean -fX

# Check if file would be ignored
git check-ignore filename

# List all ignored files
git status --ignored
```

### Online Tools
- [gitignore.io](https://gitignore.io) - Generate .gitignore templates
- [GitHub's gitignore templates](https://github.com/github/gitignore)

### Remember
- Security first: always protect credentials and secrets
- Clean repositories are happy repositories
- When in doubt, ignore it - you can always unignore later
- Review your `.gitignore` regularly as your project evolves

---

*Keep this handbook updated as new patterns and best practices emerge in your development workflow.*

---

**Made with Claude AI**  
**Date**: 02.12.2025