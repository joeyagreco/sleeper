from sleeper.util.ConfigReader import ConfigReader

SLEEPER_APP_BASE_URL = ConfigReader.get("api", "sleeper_app_base_url")
SLEEPER_CDN_BASE_URL = ConfigReader.get("api", "sleeper_cdn_base_url")
VERSION = ConfigReader.get("api", "version")

# ROUTES
AVATARS_ROUTE = ConfigReader.get("api", "avatars_route")
CONTENT_ROUTE = ConfigReader.get("api", "content_route")
DEPTH_CHART_ROUTE = ConfigReader.get("api", "depth_chart_route")
DRAFT_ROUTE = ConfigReader.get("api", "draft_route")
DRAFTS_ROUTE = ConfigReader.get("api", "drafts_route")
LEAGUE_ROUTE = ConfigReader.get("api", "league_route")
LEAGUES_ROUTE = ConfigReader.get("api", "leagues_route")
LOSERS_BRACKET_ROUTE = ConfigReader.get("api", "losers_bracket_route")
MATCHUPS_ROUTE = ConfigReader.get("api", "matchups_route")
PICKS_ROUTE = ConfigReader.get("api", "picks_route")
PLAYER_ROUTE = ConfigReader.get("api", "player_route")
PLAYERS_ROUTE = ConfigReader.get("api", "players_route")
PROJECTIONS_ROUTE = ConfigReader.get("api", "projections_route")
ROSTERS_ROUTE = ConfigReader.get("api", "rosters_route")
SCHEDULE_ROUTE = ConfigReader.get("api", "schedule_route")
STATE_ROUTE = ConfigReader.get("api", "state_route")
STATS_ROUTE = ConfigReader.get("api", "stats_route")
THUMBS_ROUTE = ConfigReader.get("api", "thumbs_route")
TRADED_PICKS_ROUTE = ConfigReader.get("api", "traded_picks_route")
TRANSACTIONS_ROUTE = ConfigReader.get("api", "transactions_route")
TRENDING_ROUTE = ConfigReader.get("api", "trending_route")
USER_ROUTE = ConfigReader.get("api", "user_route")
USERS_ROUTE = ConfigReader.get("api", "users_route")
WINNERS_BRACKET_ROUTE = ConfigReader.get("api", "winners_bracket_route")


# DEFAULTS
DEFAULT_TRENDING_PLAYERS_LOOKBACK_HOURS = 24
DEFAULT_TRENDING_PLAYERS_LIMIT = 25
