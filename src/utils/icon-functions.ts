import icons from "../resources/arsha-icon-ids.json";

export function getIconUrl(itemId: number): string | undefined {
  if (itemId in icons) {
    return `https:\\cdn.arsha.io/icons/${itemId}.png`;
  }
}
