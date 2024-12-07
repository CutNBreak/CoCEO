# Dependency Map

This document tracks external dependencies, their versions, purposes, and relationships within the project.

## Core Dependencies

### Project Configuration
- **pyproject.toml**: Main dependency and project configuration file
  - Status: To be analyzed
  - Location: Root directory
  - Purpose: Python project metadata and dependency management

### Development Environment
- **pre-commit**: Indicated by `.pre-commit-config.yaml`
  - Status: To be analyzed
  - Location: Root directory
  - Purpose: Git hooks for code quality checks

### Containerization
- **Docker**: Indicated by `Dockerfile`
  - Status: To be analyzed
  - Location: Root directory
  - Purpose: Container configuration for deployment/development

## Integration Points

### Language Model Providers
Based on documentation in `docs/language-models/hosted-models/`:

1. **OpenAI**
   - Status: To be analyzed
   - Integration Point: LLM provider
   - Documentation: docs/language-models/hosted-models/openai.mdx

2. **Anthropic**
   - Status: To be analyzed
   - Integration Point: LLM provider
   - Documentation: docs/language-models/hosted-models/anthropic.mdx

3. **Azure**
   - Status: To be analyzed
   - Integration Point: LLM provider
   - Documentation: docs/language-models/hosted-models/azure.mdx

*(Additional providers listed in documentation to be analyzed)*

### Local Model Support
Based on documentation in `docs/language-models/local-models/`:

1. **Ollama**
   - Status: To be analyzed
   - Integration Point: Local model support
   - Documentation: docs/language-models/local-models/ollama.mdx

2. **LM Studio**
   - Status: To be analyzed
   - Integration Point: Local model support
   - Documentation: docs/language-models/local-models/lm-studio.mdx

## Dependency Analysis Status

### To Be Analyzed
- Exact Python package dependencies from pyproject.toml
- Development dependencies
- Optional dependencies
- Version constraints and compatibility requirements

### Known Integration Requirements
- Docker support
- Git and pre-commit hooks
- Multiple LLM provider APIs
- Local model integration capabilities

## Version Management

### Version Control
- Git (indicated by .gitignore)
- Pre-commit hooks for quality control

### Dependency Versioning
To be determined from pyproject.toml analysis:
- Required Python version
- Package version constraints
- Compatible LLM API versions

## Integration Architecture

### Current Understanding
- Modular design with pluggable LLM providers
- Support for both hosted and local models
- Container-based deployment option
- Development environment standardization through pre-commit

### Areas Needing Investigation
1. Dependency injection patterns
2. Plugin architecture for LLM providers
3. Configuration management
4. Version compatibility matrix

## Dependency Maintenance

### Monitoring Needed
- Security updates for dependencies
- LLM API version changes
- Docker base image updates
- Pre-commit hook updates

### Update Strategy
To be determined:
- Dependency update frequency
- Breaking change management
- Backward compatibility requirements
- Testing strategy for updates

## Next Steps

1. Analyze pyproject.toml for exact dependencies
2. Review Docker configuration
3. Document LLM provider integration requirements
4. Map dependency relationships and conflicts
5. Establish version compatibility matrix

## Change Log
- Initial creation: Documented visible dependencies from project structure
- Next review: After pyproject.toml analysis

## Notes
This is a living document that will be updated as we:
1. Analyze configuration files
2. Review integration code
3. Discover additional dependencies
4. Validate assumptions about integrations
