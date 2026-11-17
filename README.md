# ScoringInfo (retired)

This site is retired. The Flight Coach Score documentation has moved to
[FCScoreDocs](https://pyflightcoach.github.io/FCScoreDocs/).

This repository now serves only two things from `site/`, published to GitHub Pages:

- `help/*.md`: copies of the help files for deployed FCScore clients, which fetch
  `https://pyflightcoach.github.io/ScoringInfo/help/<name>.md`. These paths must not change.
- Redirect pages for the old ScoringInfo URLs, plus `404.html`, which send
  visitors to FCScoreDocs.

## Refreshing help files

With an FCScoreDocs checkout next to this one:

```sh
python3 scripts/sync_help.py --docs ../FCScoreDocs
python3 scripts/sync_help.py --check   # exit 1 if site/help is out of date
```

The sync rewrites the FCScoreDocs placeholders (`/fcsdocsbase`, `/fcscorebase`) into
absolute links for the old clients. It never deletes a file from `site/help`; orphaned
files produce a warning.

## Regenerating redirects

Edit the `REDIRECTS` mapping at the top of `scripts/make_redirects.py`, then run:

```sh
python3 scripts/make_redirects.py
```

## Deployment

Pushing to `main` uploads `site/` as a Pages artifact and deploys it. There is no build step.

## Archiving

This repository will be archived after the FCScore main cutover, once no deployed client
uses `/ScoringInfo/help`. Check that before archiving.
