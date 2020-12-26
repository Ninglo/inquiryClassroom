// pages/questionquery/questionquery.js
Page({

  /**
   * Page initial data
   */
  data: {
    questionMessage: '',
    questions: [],
    changed: false,
  },

  messageChange: function (e) {
    const value = e.detail.value
    this.setData({
      changed: true,
      questionMessage: e.detail.value
    })
    console.log(this.__data__.questions)
  },
  query: function () {
    if (!this.__data__.changed) return;
    this.setData({
      changed: false,
    })
    const that = this
    wx.request({
      url: `https://zzkf.mynatapp.cc/api?question=${that.__data__.questionMessage}`,
      success: (data) => {
        const resData = [data.data]
        resData[0].tm = resData[0].tm.replace(/\<br\>/g, '\n')
        console.log(resData[0].tm)
        const newData = resData.concat(this.__data__.questions)
        this.setData({
          questions: newData,
        })
      }
    })
  },

  /**
   * Lifecycle function--Called when page load
   */
  onLoad: function (options) {

  },

  /**
   * Lifecycle function--Called when page is initially rendered
   */
  onReady: function () {

  },

  /**
   * Lifecycle function--Called when page show
   */
  onShow: function () {

  },

  /**
   * Lifecycle function--Called when page hide
   */
  onHide: function () {

  },

  /**
   * Lifecycle function--Called when page unload
   */
  onUnload: function () {

  },

  /**
   * Page event handler function--Called when user drop down
   */
  onPullDownRefresh: function () {

  },

  /**
   * Called when page reach bottom
   */
  onReachBottom: function () {

  },

  /**
   * Called when user click on the top right corner to share
   */
  onShareAppMessage: function () {

  }
})