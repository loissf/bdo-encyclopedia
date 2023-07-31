import { ListItem } from "@/models/Item";
import { defineStore } from "pinia";
import { computed, ref } from "vue";

export const useMarketStore = defineStore("market", () => {
  const _listItems = ref<ListItem[]>([]);
  const listItems = computed({
    get: () => {
      return _listItems.value;
    },

    set: (value: ListItem[]) => {
      _listItems.value = value;
    },
  });

  const _viewType = ref<string>("");
  const viewType = computed({
    get: () => {
      return _viewType.value;
    },

    set: (value: string) => {
      _viewType.value = value;
    },
  });

  return {
    listItems,
    viewType,
  };
});
