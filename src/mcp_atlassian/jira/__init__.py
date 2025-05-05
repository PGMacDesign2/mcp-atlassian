"""Jira API module for mcp_atlassian.

This module provides various Jira API client implementations.
"""

# flake8: noqa

# Re-export the Jira class for backward compatibility
from atlassian.jira import Jira

from .client import JiraClient
from .comments import CommentsMixin
from .config import JiraConfig
from .epics import EpicsMixin
from .fields import FieldsMixin
from .formatting import FormattingMixin
from .issues import IssuesMixin
from .links import LinksMixin
from .projects import ProjectsMixin
from .search import SearchMixin
from .sprints import SprintsMixin
from .transitions import TransitionsMixin
from .users import UsersMixin
from .worklog import WorklogMixin
from .boards import BoardsMixin
from .attachments import AttachmentsMixin


class JiraFetcher(
    ProjectsMixin,
    FieldsMixin,
    FormattingMixin,
    TransitionsMixin,
    WorklogMixin,
    EpicsMixin,
    CommentsMixin,
    SearchMixin,
    IssuesMixin,
    UsersMixin,
    BoardsMixin,
    SprintsMixin,
    AttachmentsMixin,
    LinksMixin,
):
    """
    The main Jira client class providing access to all Jira operations.

    This class inherits from multiple mixins that provide specific functionality:
    - ProjectsMixin: Project-related operations
    - FieldsMixin: Field-related operations
    - FormattingMixin: Content formatting utilities
    - TransitionsMixin: Issue transition operations
    - WorklogMixin: Worklog operations
    - EpicsMixin: Epic operations
    - CommentsMixin: Comment operations
    - SearchMixin: Search operations
    - IssuesMixin: Issue operations
    - UsersMixin: User operations
    - BoardsMixin: Board operations
    - SprintsMixin: Sprint operations
    - AttachmentsMixin: Attachment download operations
    - LinksMixin: Issue link operations

    The class structure is designed to maintain backward compatibility while
    improving code organization and maintainability.
    """

    pass


# Utility functions for custom fields management
def register_jira_custom_field(jira_client: JiraFetcher, field_name_or_id: str) -> str | None:
    """
    Register a custom field for inclusion in Jira API requests.
    
    Args:
        jira_client: The JiraFetcher instance
        field_name_or_id: Name or ID of the custom field to register
        
    Returns:
        The field ID if registration was successful, None otherwise
    """
    return jira_client.register_custom_field(field_name_or_id)


def list_jira_custom_fields(jira_client: JiraFetcher) -> list[str]:
    """
    List all registered custom fields.
    
    Args:
        jira_client: The JiraFetcher instance
        
    Returns:
        List of custom field IDs currently registered
    """
    return jira_client.get_custom_fields_list()


def clear_jira_custom_fields(jira_client: JiraFetcher) -> None:
    """
    Clear all registered custom fields.
    
    Args:
        jira_client: The JiraFetcher instance
    """
    jira_client.clear_custom_fields()


__all__ = [
    "JiraFetcher", 
    "JiraConfig", 
    "JiraClient", 
    "Jira",
    "register_jira_custom_field",
    "list_jira_custom_fields",
    "clear_jira_custom_fields",
]
