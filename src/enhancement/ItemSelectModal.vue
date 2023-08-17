<template>
  <div class="modal">
    <div class="content">
      <div v-if="!selectedItem" class="item-search">
        <input
          type="text"
          name="search-box"
          id="search-box"
          v-model="searchTerm"
        />
        <ul v-if="searchResult?.length" class="search-results">
          <li
            v-for="item in searchResult"
            :key="item.id"
            @click="selectItem(item)"
          >
            <!-- <img class="icon" :src="item.icon" :width="40" /> -->
            <ItemIcon :item-id="item.id" :item-grade="item.grade" />
            <span class="name">{{ item.name }}</span>
          </li>
        </ul>
      </div>
      <template v-else>
        <div class="selected-item">
          <div class="item">
            <!-- <img class="icon" :src="selectedItem.icon" :width="40" /> -->
            <ItemIcon
              :item-id="selectedItem.id"
              :item-grade="selectedItem.grade"
              :enhancement="selectedEnhancement"
            />
            <ItemName
              class="name"
              :item-id="selectedItem.id"
              :item-name="selectedItem.name"
              :item-grade="0"
              :enhancement="selectedEnhancement"
            />
            <button class="clear-button" @click="clearSelectedItem">
              &larr;
            </button>
          </div>
        </div>
        <div class="settings">
          <div class="setting">
            <label for="amount">Quantity</label>
            <NumericSelector id="amount" :min="1" v-model="selectedQuantity" />
          </div>
          <div class="setting">
            <label for="lvl">Enhancement</label>
            <NumericSelector
              id="lvl"
              :min="0"
              :max="maxEnhancement"
              v-model="selectedEnhancement"
            />
          </div>
        </div>
      </template>
    </div>
    <div class="footer">
      <button
        @click="
          emits('close', {
            selectedItem,
            selectedQuantity,
            selectedEnhancement,
          })
        "
        class="accept-button"
        :class="!selectedItem ? 'disabled' : ''"
      >
        ACCEPT
      </button>
      <button @click="emits('close', false)" class="cancel-button">
        CANCEL
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";

import { searchItem } from "@/utils/item-functions";

import { getAvaliableEnhancements } from "@/queries";
import { DictionaryItem } from "@/models/Item";

import NumericSelector from "@/components/NumericSelector.vue";
import ItemIcon from "@/components/ItemIcon.vue";
import ItemName from "@/components/ItemName.vue";

const emits = defineEmits(["close"]);

const searchTerm = ref<string>("");
const searchResult = ref<DictionaryItem[]>();

const selectedItem = ref<DictionaryItem>();
const selectedQuantity = ref<number>();
const selectedEnhancement = ref<number>();

const maxEnhancement = ref<number>();

watch(selectedItem, (item) => {
  if (item) {
    getAvaliableEnhancements(item.id).then(
      (value) => (maxEnhancement.value = value[value.length - 1] + 1)
    );
  }
});

watch(searchTerm, (value) => {
  if (!value) {
    searchResult.value = [];
    return;
  }

  searchResult.value = searchItem(value);
});

function selectItem(item: DictionaryItem) {
  selectedItem.value = item;
}

function clearSelectedItem() {
  selectedItem.value = undefined;
}
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.modal {
  @include floating-section;

  color: white;

  display: flex;
  flex-direction: column;

  width: 25rem;
  height: min-content;

  justify-content: space-between;

  padding: 1rem;

  gap: 1.5rem;

  .content {
    display: flex;
    flex-direction: column;
    justify-content: center;

    flex-grow: 1;

    .selected-item {
      .item {
        display: flex;

        align-items: center;

        gap: 0.5rem;

        padding: 0.25rem 0.5rem;

        font-size: 120%;

        .icon {
          border: 2px dashed rgb(122, 122, 122);
          border-radius: 6px;
        }

        .name {
          flex-grow: 1;

          white-space: nowrap;
          text-overflow: ellipsis;
        }

        .clear-button {
          color: white;
          background: transparent;
          border-radius: 12px;
        }
      }
    }

    .settings {
      display: flex;
      flex-direction: row;

      justify-content: space-around;

      margin: 0.5rem 0;
      flex-grow: 1;

      .setting {
        display: flex;
        flex-direction: column;

        @include flex-center-all;

        gap: 1rem;
      }
    }

    .item-search {
      position: relative;

      #search-box {
        @include input-element;
        width: 100%;
      }

      .search-results {
        @include custom-scrollbar;

        background-color: #2b2b2b;
        box-shadow: 4px 4px 24px 0px rgba(0, 0, 0, 0.75);

        width: 96%;

        position: absolute;

        max-height: 16rem;
        overflow-y: auto;

        padding: 0.5rem;
        margin: 0;

        li {
          display: flex;

          align-items: center;

          gap: 0.5rem;

          padding: 0.25rem 0.5rem;

          &:hover {
            background-color: rgb(36, 36, 36);
          }

          .icon {
            border: 2px dashed rgb(122, 122, 122);
            border-radius: 6px;
          }
        }
      }
    }
  }

  .footer {
    display: flex;
    flex-direction: row;

    justify-content: space-around;

    gap: 2rem;

    button {
      width: 100%;

      color: white;
      border: none;

      border-radius: 6px;

      height: 2rem;

      &.accept-button {
        background-color: rgb(73, 150, 73);
      }

      &.cancel-button {
        background-color: rgb(189, 80, 80);
      }

      &.disabled {
        background-color: gray;
      }
    }
  }
}
</style>
