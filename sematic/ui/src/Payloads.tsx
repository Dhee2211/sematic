import { Run, Artifact, Edge } from "./Models";

export type RunListPayload = {
  current_page_url: string;
  next_page_url?: string;
  limit: number;
  next_cursor?: string;
  after_cursor_count: number;
  content: Run[];
};

export type RunViewPayload = {
  content: Run;
};

export type ArtifactMap = {
  input: Map<string, Artifact>;
  output: Map<string, Artifact>;
};

export type RunArtifactMap = Map<string, ArtifactMap>;

export type ArtifactListPayload = {
  content: Artifact[];
};

export type EdgeListPayload = {
  content: Edge[];
};

export type RunGraphPayload = {
  root_id: string;
  runs: Run[];
  edges: Edge[];
  artifacts: Artifact[];
};