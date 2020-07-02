const db = wx.cloud.database()
var classroomData

Page({
  /**
   * 页面的初始数据
   */
  data: {
  },

  /**
   * 点击日期展开当日考试时间
   */
  showDateDetail: function (req) {
    var date = req.currentTarget.dataset.date
    this.setData({
      showDate: date
    })
  },

  /**
   * 选择时间段显示考试教室
   */
  radioChange(req) {
    var rooms = classroomData[req.detail.value]
    var roomD = []
    var roomE = []
    var roomOther = []

    for (var i = 0; i < rooms.length; i++)
    {
      var room = rooms[i]
      if (room.search('D') != -1)
      {
        roomD.push(room)
      }
      else
      {
        if (room.search('E') != -1)
        {
          roomE.push(room)
        }
        else
        {
          roomOther.push(room)
        }
      }
    }
    this.setData({
      roomD: roomD,
      roomE: roomE,
      roomOther: roomOther
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    db.collection('inquiry')
      .where({
      })
      .get({
        success: function (res) {
          for (var i = 0; i < res.data.length; i++)
          {
            var data = res.data[i]
            var name = data.name
            switch (name)
            {
              case 'dateIndex':
                that.setData({
                  dateIndex: data
                })
                break

              case 'timeIndex':
                that.setData({
                  timeIndex: data
                })
                break

              default:
                classroomData = data
                break
            }
          }

        }
      })
  },


  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
