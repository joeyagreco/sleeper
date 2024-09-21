from sleeper.api import (
    get_draft,
    get_drafts_in_league,
    get_player_draft_picks,
    get_traded_draft_picks,
    get_user_drafts_for_year,
)

if __name__ == "__main__":
    # get all drafts that a user was in for a particular year
    user_drafts = get_user_drafts_for_year(user_id="my_user_id", sport="nfl", year=2020)

    # get all drafts for a particular league
    league_drafts = get_drafts_in_league(league_id="my_league_id")

    # get a draft by its ID
    draft = get_draft(draft_id="my_draft_id")

    # get all draft picks for a particular draft
    draft_picks = get_player_draft_picks(
        draft_id="my_draft_id",
    )

    # get all traded draft picks for a particular draft
    traded_draft_picks = get_traded_draft_picks(draft_id="my_draft_id")
