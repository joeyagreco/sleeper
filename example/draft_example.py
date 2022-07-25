from sleeper import DraftAPIClient
from sleeper.enum.Sport import Sport
from sleeper.model.Draft import Draft
from sleeper.model.DraftPick import DraftPick
from sleeper.model.PlayerDraftPick import PlayerDraftPick

if __name__ == "__main__":
    # get all drafts that a user was in for a particular year
    user_drafts: list[Draft] = DraftAPIClient.get_user_drafts_for_year(user_id="my_user_id", sport=Sport.NFL,
                                                                       year="2020")

    # get all drafts for a particular league
    league_drafts: list[Draft] = DraftAPIClient.get_drafts_in_league(league_id="my_league_id")

    # get a draft by its ID
    draft: Draft = DraftAPIClient.get_draft(draft_id="my_draft_id")

    # get all draft picks for a particular draft
    draft_picks: list[PlayerDraftPick] = DraftAPIClient.get_player_draft_picks(draft_id="my_draft_id", sport=Sport.NFL)

    # get all traded draft picks for a particular draft
    traded_draft_picks: list[DraftPick] = DraftAPIClient.get_traded_draft_picks(draft_id="my_draft_id")
