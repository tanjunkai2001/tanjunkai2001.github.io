import gsbg

article_link = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=KrOQdKAAAAAJ&citation_for_view=KrOQdKAAAAAJ:W7OEmFMy1HYC"
profile_link = "https://scholar.google.com/citations?user=KrOQdKAAAAAJ&hl=en"

article_citation_num = gsbg.fetch_article_citation_num(article_link)
profile_citation_num = gsbg.fetch_profile_citation_num(profile_link)
gsbg.gene_citation_badge_link(
    link='https://scholar.google.com/citations?user=KrOQdKAAAAAJ&hl=en', 
    link_type="profile",
)
gsbg.gene_citation_badge_svg(
    link='https://scholar.google.com/citations?user=KrOQdKAAAAAJ&hl=en', 
    link_type="profile",
    svg_name='gsbg.svg',
    path_to_save='generated_badges',
)