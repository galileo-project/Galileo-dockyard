from dockyard.handler.api.public.github import PublicGitHubHandeler


routes = [(r"/api/public/github/(.*)",        PublicGitHubHandeler)]